"""XiaoYuan Financial Derivative Data Model."""

from typing import Any, Dict, List, Optional, Literal
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError

from openbb_xiaoyuan.standard_models.financial_derivative_data import (
    FinancialDerivativeQueryParams,
    FinancialDerivativeData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    extractMonthDayFromTime,
)


class XiaoYuanFinancialDerivativeQueryParams(FinancialDerivativeQueryParams):
    """XiaoYuan Financial Derivative Query."""

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


class XiaoYuanFinancialDerivativeData(FinancialDerivativeData):
    """XiaoYuan Finance Cash Flow Statement Data."""

    __alias_dict__ = {
        "non_interest_bearing_current_liabilities": "无息流动负债",
        "non_interest_bearing_non_current_liabilities": "无息非流动负债",
        "interest_bearing_debt": "带息债务",
        "net_debt": "净债务",
        "tangible_net_assets": "有形净资产",
        "working_capital": "营运资本",
        "net_working_capital": "净营运资本",
        "retained_earnings": "留存收益",
        "gross_profit": "毛利",
        "net_operating_income": "经营活动净收益",
        "net_income_from_fair_value_changes": "价值变动净收益",
        "ebit": "息税前利润",
        "ebitda": "息税折旧摊销前利润",
        "non_recurring_gains_and_losses": "非经常性损益",
        "net_profit_attributable_to_shareholders_excl_non_recurring_gains_and_losses": "扣除非经常性损益后的归属于上市公司股东的净利润",
        "free_cash_flow_to_firm": "企业自由现金流量",
        "free_cash_flow_to_equity": "股权自由现金流量",
        "depreciation_and_amortization": "折旧与摊销",
        "period_ending": "报告期",
    }


class XiaoYuanFinancialDerivativeFetcher(
    Fetcher[
        XiaoYuanFinancialDerivativeQueryParams,
        List[XiaoYuanFinancialDerivativeData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinancialDerivativeQueryParams:
        """Transform the query parameters."""

        return XiaoYuanFinancialDerivativeQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinancialDerivativeQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""

        factors = [
            "无息流动负债",
            "无息非流动负债",
            "带息债务",
            "净债务",
            "有形净资产",
            "营运资本",
            "净营运资本",
            "留存收益",
            "毛利",
            "经营活动净收益",
            "价值变动净收益",
            "息税前利润",
            "息税折旧摊销前利润",
            "非经常性损益",
            "扣除非经常性损益后的归属于上市公司股东的净利润",
            "企业自由现金流量",
            "股权自由现金流量",
            "折旧与摊销",
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
        query: XiaoYuanFinancialDerivativeQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinancialDerivativeData]:
        """Transform the data."""

        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanFinancialDerivativeData.model_validate(d) for d in data]
