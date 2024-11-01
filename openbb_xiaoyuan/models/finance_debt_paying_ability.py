"""XiaoYuan Finance Debt Paying Ability Model."""

from typing import Any, Dict, List, Optional, Literal

import pandas as pd
from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field

from openbb_xiaoyuan.standard_models.finance_debt_paying_ability import (
    FinanceDebtpayingAbilityQueryParams,
    FinanceDebtpayingAbilityData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    extractMonthDayFromTime,
)


class XiaoYuanFinanceDebtpayingAbilityQueryParams(FinanceDebtpayingAbilityQueryParams):
    """XiaoYuan Finance Debt Paying Ability Query."""

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


class XiaoYuanFinanceDebtpayingAbilityData(FinanceDebtpayingAbilityData):
    """XiaoYuan Finance Debt Paying Ability Data."""

    __alias_dict__ = {
        "debt_to_asset_ratio": "资产负债率",
        "conservative_quick_ratio": "保守速动比率",
        "equity_to_debt_ratio": "产权比率",
        "shareholder_equity_to_interest_bearing_debt": "归属母公司股东的权益比带息债务",
        "shareholder_equity_to_total_liabilities": "归属母公司股东的权益比负债合计",
        "net_cash_flow_from_operating_activities_to_interest_bearing_debt": "经营活动产生的现金流量净额比带息债务",
        "net_cash_flow_from_operating_activities_to_total_liabilities": "经营活动产生的现金流量净额比负债合计",
        "net_cash_flow_from_operating_activities_to_net_debt": "经营活动产生的现金流量净额比净债务",
        "net_cash_flow_from_operating_activities_to_current_liabilities": "经营活动产生的现金流量净额比流动负债",
        "current_ratio": "流动比率",
        "quick_ratio": "速动比率",
        "tangible_assets_to_interest_bearing_debt": "有形资产比带息债务",
        "tangible_assets_to_total_liabilities": "有形资产比负债合计",
        "tangible_assets_to_net_debt": "有形资产比净债务",
        "period_ending": "报告期",
    }


class XiaoYuanFinanceDebtpayingAbilityFetcher(
    Fetcher[
        XiaoYuanFinanceDebtpayingAbilityQueryParams,
        List[XiaoYuanFinanceDebtpayingAbilityData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinanceDebtpayingAbilityQueryParams:
        """Transform the query parameters."""
        return XiaoYuanFinanceDebtpayingAbilityQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceDebtpayingAbilityQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = [
            "资产负债率",
            "保守速动比率",
            "产权比率",
            "归属母公司股东的权益比带息债务",
            "归属母公司股东的权益比负债合计",
            "经营活动产生的现金流量净额比带息债务",
            "经营活动产生的现金流量净额比负债合计",
            "经营活动产生的现金流量净额比净债务",
            "经营活动产生的现金流量净额比流动负债",
            "流动比率",
            "速动比率",
            "有形资产比带息债务",
            "有形资产比负债合计",
            "有形资产比净债务",
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
        query: XiaoYuanFinanceDebtpayingAbilityQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceDebtpayingAbilityData]:
        """Transform the data ."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanFinanceDebtpayingAbilityData.model_validate(d) for d in data]
