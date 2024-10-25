"""XiaoYuan Finance Profitability Model."""

from typing import Any, Dict, List, Optional, Literal

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field

from openbb_xiaoyuan.standard_models.finance_profit_ability import (
    FinanceProfitAbilityQueryParams,
    FinanceProfitAbilityData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    groupByTime_sql,
)


class XiaoYuanFinanceProfitAbilityQueryParams(FinanceProfitAbilityQueryParams):
    """XiaoYuan Finance Profitability Query."""

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


class XiaoYuanFinanceProfitAbilityData(FinanceProfitAbilityData):
    """XiaoYuan Finance Profitability Data."""

    __alias_dict__ = {
        "roe_diluted_percent": "净资产收益率ROE（摊薄）（百分比）",
        "roe_average_percent": "净资产收益率ROE（平均）（百分比）",
        "roe_weighted_percent": "净资产收益率ROE（加权）（百分比）",
        "roe_ex_diluted_percent": "净资产收益率ROE（扣除比摊薄）（百分比）",
        "roe_ex_weighted_percent": "净资产收益率ROE（扣除比加权）（百分比）",
        "roa_net_percent": "总资产净利率ROA（百分比）",
        "roa_return_percent": "总资产报酬率ROA（百分比）",
        "roic_percent": "投入资本回报率ROIC（百分比）",
        "roe_ttm_percent": "净资产收益率ROE（TTM）（百分比）",
        "roa_return_ttm_percent": "总资产报酬率ROA（TTM）（百分比）",
        "roa_net_ttm_percent": "总资产净利率（TTM）（百分比）",
        "net_profit_margin_percent": "销售净利率（百分比）",
        "net_profit_margin_ttm_percent": "销售净利率（TTM）（百分比）",
        "gross_profit_margin_percent": "销售毛利率（百分比）",
        "gross_profit_margin_ttm_percent": "销售毛利率（TTM）（百分比）",
        "selling_expenses_to_revenue_percent": "销售期间费用率（百分比）",
        "selling_expenses_to_revenue_ttm_percent": "销售期间费用率（TTM）（百分比）",
        "net_profit_to_total_revenue_percent": "净利润比营业总收入（百分比）",
        "net_profit_to_total_revenue_ttm_percent": "净利润比营业总收入（TTM）（百分比）",
        "operating_profit_to_total_revenue_percent": "营业利润比营业总收入（百分比）",
        "operating_profit_to_total_revenue_ttm_percent": "营业利润比营业总收入（TTM）（百分比）",
        "total_cost_to_revenue_ttm_percent": "营业总成本比营业总收入（TTM）（百分比）",
        "selling_expenses_to_total_revenue_ttm_percent": "营业费用比营业总收入（TTM）（百分比）",
        "admin_expenses_to_total_revenue_ttm_percent": "管理费用比营业总收入（TTM）（百分比）",
        "financial_expenses_to_total_revenue_ttm_percent": "财务费用比营业总收入（TTM）（百分比）",
        "impairment_losses_to_total_revenue_ttm_percent": "资产减值损失比营业总收入（TTM）（百分比）",
        "roe_ex_ttm_percent": "净资产收益率ROETTM（扣非）（百分比）",
        "roic_ttm_percent": "投入资本回报率ROIC（TTM）（百分比）",
        "cost_to_profit_ratio_percent": "成本费用利润率（百分比）",
        "r_and_d_expenses_to_revenue_percent": "研发费用比营业总收入（百分比）",
        "period_ending": "报告期",
    }


class XiaoYuanFinanceProfitAbilityFetcher(
    Fetcher[
        XiaoYuanFinanceProfitAbilityQueryParams,
        List[XiaoYuanFinanceProfitAbilityData],
    ]
):
    """"""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinanceProfitAbilityQueryParams:
        """Transform the query parameters."""
        return XiaoYuanFinanceProfitAbilityQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceProfitAbilityQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = [
            "净资产收益率ROE（摊薄）（百分比）",
            "净资产收益率ROE（平均）（百分比）",
            "净资产收益率ROE（加权）（百分比）",
            "净资产收益率ROE（扣除比摊薄）（百分比）",
            "净资产收益率ROE（扣除比加权）（百分比）",
            "总资产净利率ROA（百分比）",
            "总资产报酬率ROA（百分比）",
            "投入资本回报率ROIC（百分比）",
            "净资产收益率ROE（TTM）（百分比）",
            "总资产报酬率ROA（TTM）（百分比）",
            "总资产净利率（TTM）（百分比）",
            "销售净利率（百分比）",
            "销售净利率（TTM）（百分比）",
            "销售毛利率（百分比）",
            "销售毛利率（TTM）（百分比）",
            "销售期间费用率（百分比）",
            "销售期间费用率（TTM）（百分比）",
            "净利润比营业总收入（百分比）",
            "净利润比营业总收入（TTM）（百分比）",
            "营业利润比营业总收入（百分比）",
            "营业利润比营业总收入（TTM）（百分比）",
            "营业总成本比营业总收入（TTM）（百分比）",
            "营业费用比营业总收入（TTM）（百分比）",
            "管理费用比营业总收入（TTM）（百分比）",
            "财务费用比营业总收入（TTM）（百分比）",
            "资产减值损失比营业总收入（TTM）（百分比）",
            "净资产收益率ROETTM（扣非）（百分比）",
            "投入资本回报率ROIC（TTM）（百分比）",
            "成本费用利润率（百分比）",
            "研发费用比营业总收入（百分比）",
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
        query: XiaoYuanFinanceProfitAbilityQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceProfitAbilityData]:
        """Transform the data."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanFinanceProfitAbilityData.model_validate(d) for d in data]
