"""XiaoYuan Finance Growth Ability Model."""

from typing import Any, Dict, List, Optional, Literal

import pandas as pd
from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field

from openbb_xiaoyuan.standard_models.finance_growth_ability import (
    FinanceGrowthAbilityQueryParams,
    FinanceGrowthAbilityData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    groupByTime_sql,
)


class XiaoYuanFinanceGrowthAbilityQueryParams(FinanceGrowthAbilityQueryParams):
    """XiaoYuan Finance Growth Ability Query."""

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


class XiaoYuanFinanceGrowthAbilityData(FinanceGrowthAbilityData):
    """XiaoYuan Finance Growth Ability Data."""

    __alias_dict__ = {
        "total_asset_yoy_growth_rate_percent": "总资产同比增长率（百分比）",
        "total_revenue_yoy_growth_rate_percent": "营业总收入同比增长率（百分比）",
        "operating_profit_yoy_growth_rate_percent": "营业利润同比增长率（百分比）",
        "total_profit_yoy_growth_rate_percent": "利润总额同比增长率（百分比）",
        "net_profit_yoy_growth_rate_percent": "净利润同比增长率（百分比）",
        "shareholder_net_profit_yoy_growth_rate_percent": "归属母公司股东的净利润同比增长率（百分比）",
        "shareholder_net_profit_excl_nonrecurring_yoy_growth_rate_percent": "归属母公司股东的净利润同比增长率（扣非）（百分比）",
        "basic_eps_yoy_growth_rate_percent": "基本每股收益同比增长率（百分比）",
        "diluted_eps_yoy_growth_rate_percent": "稀释每股收益同比增长率（百分比）",
        "roe_yoy_growth_rate_diluted_percent": "净资产收益率同比增长率（摊薄）（百分比）",
        "net_operating_cash_flow_yoy_growth_rate_percent": "经营活动产生的现金流量净额同比增长率（百分比）",
        "net_operating_cash_flow_per_share_yoy_growth_rate_percent": "每股经营活动中产生的现金流量净额同比增长率（百分比）",
        "total_assets_relative_to_year_begin_growth_rate_percent": "资产总计相对年初增长率（百分比）",
        "shareholder_equity_relative_to_year_begin_growth_rate_percent": "归属母公司股东的权益相对年初增长率（百分比）",
        "net_assets_per_share_relative_to_year_begin_growth_rate_percent": "每股净资产相对年初增长率（百分比）",
        "revenue_qoq_growth_rate_percent": "营业收入环比增长率（百分比）",
        "shareholder_net_profit_rolling_qoq_growth_rate_percent": "归属净利润滚动环比增长（百分比）",
        "shareholder_net_profit_excl_nonrecurring_qoq_growth_rate_percent": "归属母公司股东的净利润环比增长率（扣非）（百分比）",
        "period_ending": "报告期",
    }


class XiaoYuanFinanceGrowthAbilityFetcher(
    Fetcher[
        XiaoYuanFinanceGrowthAbilityQueryParams,
        List[XiaoYuanFinanceGrowthAbilityData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinanceGrowthAbilityQueryParams:
        """Transform the query parameters."""
        return XiaoYuanFinanceGrowthAbilityQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceGrowthAbilityQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = [
            "总资产同比增长率（百分比）",
            "营业总收入同比增长率（百分比）",
            "营业利润同比增长率（百分比）",
            "利润总额同比增长率（百分比）",
            "净利润同比增长率（百分比）",
            "归属母公司股东的净利润同比增长率（百分比）",
            "归属母公司股东的净利润同比增长率（扣非）（百分比）",
            "基本每股收益同比增长率（百分比）",
            "稀释每股收益同比增长率（百分比）",
            "净资产收益率同比增长率（摊薄）（百分比）",
            "经营活动产生的现金流量净额同比增长率（百分比）",
            "每股经营活动中产生的现金流量净额同比增长率（百分比）",
            "资产总计相对年初增长率（百分比）",
            "归属母公司股东的权益相对年初增长率（百分比）",
            "每股净资产相对年初增长率（百分比）",
            "营业收入环比增长率（百分比）",
            "归属净利润滚动环比增长（百分比）",
            "归属母公司股东的净利润环比增长率（扣非）（百分比）",
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
        query: XiaoYuanFinanceGrowthAbilityQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceGrowthAbilityData]:
        """Transform the data."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanFinanceGrowthAbilityData.model_validate(d) for d in data]
