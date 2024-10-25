"""XiaoYuan DuPontAnalysis Model."""

from typing import Any, Dict, List, Optional, Literal

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field

from openbb_xiaoyuan.standard_models.du_pont_analysis import (
    DuPontAnalysisQueryParams,
    DuPontAnalysisData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    groupByTime_sql,
)


class XiaoYuanDuPontAnalysisQueryParams(DuPontAnalysisQueryParams):
    """XiaoYuan Finance DuPont Analysis Query."""

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


class XiaoYuanDuPontAnalysisData(DuPontAnalysisData):
    """XiaoYuan Finance DuPont Analysis Data."""

    __alias_dict__ = {
        "du_pont_analysis": "权益乘数（杜邦分析）",
        "period_ending": "报告期",
    }


class XiaoYuanDuPontAnalysisFetcher(
    Fetcher[
        XiaoYuanDuPontAnalysisQueryParams,
        List[XiaoYuanDuPontAnalysisData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XiaoYuanDuPontAnalysisQueryParams:
        """Transform the query parameters."""
        return XiaoYuanDuPontAnalysisQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanDuPontAnalysisQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = ["权益乘数（杜邦分析）"]
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
        query: XiaoYuanDuPontAnalysisQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanDuPontAnalysisData]:
        """Transform the data."""
        return [XiaoYuanDuPontAnalysisData.model_validate(d) for d in data]
