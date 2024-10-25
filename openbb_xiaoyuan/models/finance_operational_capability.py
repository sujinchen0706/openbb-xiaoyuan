"""XiaoYuan Operational Capability Model."""

from typing import Any, Dict, List, Literal, Optional

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher

from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, model_validator

from openbb_xiaoyuan.standard_models.finance_operational_capability import (
    FinanceOperationalCapabilityQueryParams,
    FinanceOperationalCapabilityData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    groupByTime_sql,
)


class XiaoYuanFinanceOperationalCapabilityQueryParams(
    FinanceOperationalCapabilityQueryParams
):
    __json_schema_extra__ = {
        "period": {
            "choices": ["fy", "q1", "q2ytd", "q3ytd", "annual"],
        }
    }

    period: Literal["fy", "q1", "q2ytd", "q3ytd", "annual"] = Field(
        default="fy",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )


class XiaoYuanFinanceOperationalCapabilityData(FinanceOperationalCapabilityData):
    """XiaoYuan Finance Operational Capability Data."""

    __alias_dict__ = {
        "fixed_asset_turnover_ratio": "固定资产周转率",
        "current_asset_turnover_ratio": "流动资产周转率",
        "total_asset_turnover_ratio": "总资产周转率",
        "inventory_turnover_ratio": "存货周转率",
        "inventory_turnover_days": "存货周转天数",
        "accounts_receivable_turnover_ratio": "应收账款周转率（含应收票据）",
        "accounts_receivable_turnover_days": "应收账款周转天数（含应收票据）",
        "operating_cycle": "营业周期",
        "accounts_payable_turnover_ratio": "应付账款周转率",
        "accounts_payable_turnover_days": "应付账款周转天数（含应付票据）",
        "period_ending": "报告期",
    }

    @model_validator(mode="before")
    @classmethod
    def replace_zero(cls, values):  # pylint: disable=no-self-argument
        """Check for zero values and replace with None."""
        return (
            {k: None if v == 0 else v for k, v in values.items()}
            if isinstance(values, dict)
            else values
        )


class XiaoYuanFinanceOperationalCapabilityFetcher(
    Fetcher[
        XiaoYuanFinanceOperationalCapabilityQueryParams,
        List[XiaoYuanFinanceOperationalCapabilityData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinanceOperationalCapabilityQueryParams:
        """Transform the query parameters."""
        return XiaoYuanFinanceOperationalCapabilityQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceOperationalCapabilityQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceOperationalCapabilityData]:
        factors = [
            "固定资产周转率",
            "流动资产周转率",
            "总资产周转率",
            "存货周转率",
            "存货周转天数",
            "应收账款周转率（含应收票据）",
            "应收账款周转天数（含应收票据）",
            "营业周期",
            "应付账款周转率",
            "应付账款周转天数（含应付票据）",
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
        df["timestamp"] = df["timestamp"].apply(lambda x: x.strftime("%Y-%m-%d"))
        df = df.sort_values(by="报告期", ascending=False)
        data = df.to_dict(orient="records")

        return data

    @staticmethod
    def transform_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceOperationalCapabilityQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceOperationalCapabilityData]:
        """Transform the data."""
        return [
            XiaoYuanFinanceOperationalCapabilityData.model_validate(d) for d in data
        ]
