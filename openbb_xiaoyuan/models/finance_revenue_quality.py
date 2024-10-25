"""XiaoYuan Finance Revenue Quality Model."""

from typing import Any, Dict, List, Optional, Literal
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError

from openbb_xiaoyuan.standard_models.finance_revenue_quality import (
    FinanceRevenueQualityQueryParams,
    FinanceRevenueQualityData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    groupByTime_sql,
)


class XiaoYuanFinanceRevenueQualityQueryParams(FinanceRevenueQualityQueryParams):
    """XiaoYuan Finance Revenue Quality Query."""

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


class XiaoYuanFinanceRevenueQualityData(FinanceRevenueQualityData):
    """XiaoYuan Finance Revenue Quality Data."""

    __alias_dict__ = {
        "net_non_operating_income_and_expenses": "营业外收支净额",
        "operating_income_to_total_profit": "经营活动净收益比利润总额",
        "value_change_net_income_to_total_profit": "价值变动净收益比利润总额",
        "non_operating_income_to_total_profit": "营业外收支净额比利润总额",
        "income_tax_to_total_profit": "所得税比利润总额",
        "net_profit_excluding_non_recurring_gains_and_losses_to_net_profit": "扣除非经常性损益的净利润比净利润",
        "operating_income_to_total_profit_ttm": "经营活动净收益比利润总额（TTM）",
        "value_change_net_income_to_total_profit_ttm": "价值变动净收益比利润总额（TTM）",
        "non_operating_income_to_total_profit_ttm": "营业外收支净额比利润总额（TTM）",
        "period_ending": "报告期",
    }


class XiaoYuanFinanceRevenueQualityFetcher(
    Fetcher[
        XiaoYuanFinanceRevenueQualityQueryParams,
        List[XiaoYuanFinanceRevenueQualityData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinanceRevenueQualityQueryParams:
        """Transform the query parameters."""
        return XiaoYuanFinanceRevenueQualityQueryParams(**params)

    @staticmethod
    def extract_data(
        query: XiaoYuanFinanceRevenueQualityQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = [
            "营业外收支净额",
            "价值变动净收益比利润总额",
            "营业外收支净额比利润总额",
            "所得税比利润总额",
            "扣除非经常性损益的净利润比净利润",
            "经营活动净收益比利润总额",
            "经营活动净收益比利润总额（TTM）",
            "价值变动净收益比利润总额（TTM）",
            "营业外收支净额比利润总额（TTM）",
        ]
        reader = get_jindata_reader()
        symbols = query.symbol.split(",")
        report_month = get_report_month(query.period)

        finance_sql = get_query_finance_sql(factors, symbols, report_month)
        df = reader._run_query(
            script=groupByTime_sql + finance_sql,
        )
        if df is None or df.empty:
            raise EmptyDataError()
        df["报告期"] = df["报告期"].apply(lambda x: x.strftime("%Y-%m-%d"))
        df = df.sort_values(by="报告期", ascending=False)
        data = df.to_dict(orient="records")
        return data

    @staticmethod
    def transform_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceRevenueQualityQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceRevenueQualityData]:
        """Transform the data."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanFinanceRevenueQualityData.model_validate(d) for d in data]
