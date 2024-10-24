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


class DuPontAnalysisQueryParams(QueryParams):
    """权益乘数（杜邦分析）"""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))


class DuPontAnalysisData(Data):
    """权益乘数（杜邦分析）"""

    symbol: str = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company."),
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get(
            "timestamp", "Reporting period publication time."
        )
    )
