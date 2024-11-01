"""XiaoYuan Finance Capital Structure Model."""

from typing import Any, Dict, List, Literal, Optional

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field

from openbb_xiaoyuan.standard_models.finance_capital_structure import (
    FinanceCapitalStructureQueryParams,
    FinanceCapitalStructureData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    extractMonthDayFromTime,
)


class XiaoYuanFinanceCapitalStructureQueryParams(FinanceCapitalStructureQueryParams):
    """XiaoYuan Finance Capital Structure Query."""

    __json_schema_extra__ = {
        "period": {
            "choices": ["fy", "q1", "q2", "q3", "annual"],
        },
    }
    period: Literal["fy", "q1", "q2", "q3", "annual"] = Field(
        default="fy",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )


class XiaoYuanFinanceCapitalStructureData(FinanceCapitalStructureData):
    """XiaoYuan Finance Capital Structure Data."""

    __alias_dict__ = {
        "current_assets_to_total_assets": "流动资产比总资产（百分比）",
        "non_current_assets_to_total_assets": "非流动资产比总资产（百分比）",
        "tangible_assets_to_total_assets": "有形资产比总资产（百分比）",
        "equity_to_total_capital": "归属母公司股东的权益比全部投入资本（百分比）",
        "interest_bearing_liabilities_to_total_capital": "带息负债比全部投入资本（百分比）",
        "current_liabilities_to_total_liabilities": "流动负债比负债合计（百分比）",
        "non_current_liabilities_to_total_liabilities": "非流动负债比负债合计（百分比）",
        "interest_bearing_debt_ratio": "有息负债率（百分比）",
        "period_ending": "报告期",
    }


class XiaoYuanFinanceCapitalStructureFetcher(
    Fetcher[
        XiaoYuanFinanceCapitalStructureQueryParams,
        List[XiaoYuanFinanceCapitalStructureData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanFinanceCapitalStructureQueryParams:
        """Transform the query parameters."""
        return XiaoYuanFinanceCapitalStructureQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceCapitalStructureQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceCapitalStructureData]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = [
            "流动资产比总资产（百分比）",
            "非流动资产比总资产（百分比）",
            "有形资产比总资产（百分比）",
            "归属母公司股东的权益比全部投入资本（百分比）",
            "带息负债比全部投入资本（百分比）",
            "流动负债比负债合计（百分比）",
            "非流动负债比负债合计（百分比）",
            "有息负债率（百分比）",
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
        df["timestamp"] = df["timestamp"].apply(lambda x: x.strftime("%Y-%m-%d"))
        df.sort_values(by="报告期", ascending=False, inplace=True)
        data = df.to_dict(orient="records")

        return data

    @staticmethod
    def transform_data(
        # pylint: disable=unused-argument
        query: XiaoYuanFinanceCapitalStructureQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[XiaoYuanFinanceCapitalStructureData]:
        """Transform the data."""
        return [XiaoYuanFinanceCapitalStructureData.model_validate(d) for d in data]
