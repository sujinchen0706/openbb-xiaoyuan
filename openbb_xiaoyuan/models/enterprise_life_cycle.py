"""XiaoYuan Enterprise Life Cycle Model."""

from typing import Any, Dict, List, Optional, Literal

import pandas as pd
from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field

from openbb_xiaoyuan.standard_models.enterprise_life_cycle import (
    EnterpriseLifeCycleQueryParams,
    EnterpriseLifeCycleData,
)
from openbb_xiaoyuan.utils.references import (
    get_report_month,
    extractMonthDayFromTime,
    get_1y_query_finance_sql,
)


class XiaoYuanEnterpriseLifeCycleQueryParams(EnterpriseLifeCycleQueryParams):
    """XiaoYuan Finance Enterprise Life Cycle Query."""

    __json_schema_extra__ = {
        "symbol": {"multiple_items_allowed": True},
        "period": {
            "choices": ["fy", "annual"],
        },
    }
    period: Literal["fy", "annual"] = Field(
        default="fy",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )

    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class XiaoYuanEnterpriseLifeCycleData(EnterpriseLifeCycleData):
    """XiaoYuan Finance Enterprise Life Cycle Data."""

    __alias_dict__ = {
        "enterprise_life_cycle": "企业生命周期",
        "period_ending": "报告期",
    }


class XiaoYuanEnterpriseLifeCycleFetcher(
    Fetcher[
        XiaoYuanEnterpriseLifeCycleQueryParams,
        List[XiaoYuanEnterpriseLifeCycleData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan Finance endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanEnterpriseLifeCycleQueryParams:
        """Transform the query parameters."""
        return XiaoYuanEnterpriseLifeCycleQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanEnterpriseLifeCycleQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract the data from the XiaoYuan Finance endpoints."""
        factors = ["企业生命周期"]
        reader = get_jindata_reader()
        symbols = query.symbol.split(",")
        report_month = get_report_month(query.period)

        finance_sql = get_1y_query_finance_sql(factors, symbols, report_month)
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
        query: XiaoYuanEnterpriseLifeCycleQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanEnterpriseLifeCycleData]:
        """Transform the data."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanEnterpriseLifeCycleData.model_validate(d) for d in data]
