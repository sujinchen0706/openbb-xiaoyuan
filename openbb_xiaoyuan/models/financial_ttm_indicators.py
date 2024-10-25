"""XiaoYuan Financial TTM Indicators Model."""

from typing import Any, Dict, List, Optional, Literal
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError

from openbb_xiaoyuan.standard_models.financial_ttm_indicators import (
    FinancialTTMIndicatorsQueryParams,
    FinancialTTMIndicatorsData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    groupByTime_sql,
)


class XiaoYuanFinancialTTMIndicatorsQueryParams(FinancialTTMIndicatorsQueryParams):
    """XiaoYuan Financial TTM Indicators Query."""

    __json_schema_extra__ = {
        "symbol": {"multiple_items_allowed": True},
        "period": {
            "choices": ["fy", "q1", "q2", "q3", "annual"],
        },
    }
    period: Literal["fy", "q1", "q2", "q3", "annual"] = Field(
        default="fy",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )

    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class XiaoYuanFinancialTTMIndicatorsData(FinancialTTMIndicatorsData):
    """XiaoYuan Financial TTM Indicators Data."""

    __alias_dict__ = {
        "total_revenue_ttm": "营业总收入TTM",
        "total_cost_ttm": "营业总成本TTM",
        "revenue_ttm": "营业收入TTM",
        "operating_cost_non_financial_ttm": "营业成本非金融类TTM",
        "operating_expenses_financial_ttm": "营业支出金融类TTM",
        "gross_profit_ttm": "毛利TTM",
        "selling_expenses_ttm": "销售费用TTM",
        "admin_expenses_ttm": "管理费用TTM",
        "financial_expenses_ttm": "财务费用TTM",
        "impairment_losses_ttm": "资产减值损失TTM",
        "net_operating_income_ttm": "经营活动净收益TTM",
        "net_income_from_fair_value_changes_ttm": "价值变动净收益TTM",
        "operating_profit_ttm": "营业利润TTM",
        "net_non_operating_income_and_expenses_ttm": "营业外收支净额TTM",
        "ebit_ttm": "息税前利润TTM",
        "total_profit_ttm": "利润总额TTM",
        "income_tax_ttm": "所得税TTM",
        "net_profit_attributable_to_shareholders_ttm": "归属母公司股东的净利润TTM",
        "period_ending": "报告期",
    }


class XiaoYuanFinancialTTMIndicatorsFetcher(
    Fetcher[
        XiaoYuanFinancialTTMIndicatorsQueryParams,
        List[XiaoYuanFinancialTTMIndicatorsData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinancialTTMIndicatorsQueryParams:
        """Transform the query parameters."""

        return XiaoYuanFinancialTTMIndicatorsQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinancialTTMIndicatorsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""

        factors = [
            "营业总收入TTM",
            "营业总成本TTM",
            "营业收入TTM",
            "营业成本非金融类TTM",
            "营业支出金融类TTM",
            "毛利TTM",
            "销售费用TTM",
            "管理费用TTM",
            "财务费用TTM",
            "资产减值损失TTM",
            "经营活动净收益TTM",
            "价值变动净收益TTM",
            "营业利润TTM",
            "营业外收支净额TTM",
            "息税前利润TTM",
            "利润总额TTM",
            "所得税TTM",
            "归属母公司股东的净利润TTM",
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
        query: XiaoYuanFinancialTTMIndicatorsQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinancialTTMIndicatorsData]:
        """Transform the data."""

        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanFinancialTTMIndicatorsData.model_validate(d) for d in data]
