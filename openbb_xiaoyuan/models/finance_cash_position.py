"""XiaoYuan Finance Cash Position Model."""

from typing import Any, Dict, List, Optional, Literal
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError

from openbb_xiaoyuan.standard_models.finance_cash_position import (
    FinanceCashpositionQueryParams,
    FinanceCashpositionData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    extractMonthDayFromTime,
)


class XiaoYuanFinanceCashpositionQueryParams(FinanceCashpositionQueryParams):
    """XiaoYuan Finance Cash Position Query."""

    __json_schema_extra__ = {
        "period": {
            "choices": ["fy", "q1", "q2ytd", "q3ytd", "annual"],
        }
    }

    period: Literal["fy", "q1", "q2ytd", "q3ytd", "annual"] = Field(
        default="fy",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )

    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class XiaoYuanFinanceCashpositionData(FinanceCashpositionData):
    """XiaoYuan Finance Cash Position Data."""

    __alias_dict__ = {
        "cash_sales_to_revenue": "销售商品提供劳务收到的现金比营业收入",
        "op_cash_to_revenue": "经营活动产生的现金流量净额比营业收入",
        "op_cash_to_income": "经营活动产生的现金流量净额比经营活动净收益",
        "capex_to_depr": "资本支出比折旧摊销",
        "cash_sales_to_revenue_ttm": "销售商品提供劳务收到的现金比营业收入（TTM）",
        "op_cash_to_revenue_ttm": "经营活动产生的现金流量净额比营业收入（TTM）",
        "op_cash_to_income_ttm": "经营活动产生的现金流量净额比经营活动净收益（TTM）",
        "op_cash_to_total_revenue": "经营活动产生的现金流量净额比营业总收入",
        "op_cash_to_net_profit": "经营活动产生的现金流量净额比净利润",
        "period_ending": "报告期",
    }


class XiaoYuanFinanceCashpositionFetcher(
    Fetcher[
        XiaoYuanFinanceCashpositionQueryParams,
        List[XiaoYuanFinanceCashpositionData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinanceCashpositionQueryParams:
        """Transform the query parameters."""
        return XiaoYuanFinanceCashpositionQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceCashpositionQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = [
            "销售商品提供劳务收到的现金比营业收入",
            "经营活动产生的现金流量净额比营业收入",
            "经营活动产生的现金流量净额比经营活动净收益",
            "资本支出比折旧摊销",
            "销售商品提供劳务收到的现金比营业收入（TTM）",
            "经营活动产生的现金流量净额比营业收入（TTM）",
            "经营活动产生的现金流量净额比经营活动净收益（TTM）",
            "经营活动产生的现金流量净额比营业总收入",
            "经营活动产生的现金流量净额比净利润",
        ]
        reader = get_jindata_reader()
        symbols = query.symbol.split(",")
        report_month = get_report_month(query.period)

        finance_sql = get_query_finance_sql(factors, symbols, report_month)
        df = reader._run_query(
            script=extractMonthDayFromTime + finance_sql,
        )
        if df is None or df.empty:
            raise EmptyDataError()
        df["报告期"] = df["报告期"].dt.strftime("%Y-%m-%d")
        df.sort_values(by="报告期", ascending=False, inplace=True)
        data = df.to_dict(orient="records")
        return data

    @staticmethod
    def transform_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceCashpositionQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceCashpositionData]:
        """Transform the data."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanFinanceCashpositionData.model_validate(d) for d in data]
