"""企业生命周期"""

from datetime import date as dateType
from typing import Optional

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class EnterpriseLifeCycleQueryParams(QueryParams):
    """企业生命周期查询参数"""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))


class EnterpriseLifeCycleData(Data):
    """企业生命周期数据"""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company.")
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get(
            "timestamp", "Reporting period publication time."
        )
    )
