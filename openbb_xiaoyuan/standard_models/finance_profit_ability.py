"""财务指标-盈利能力"""

from datetime import date as dateType
from typing import Optional

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class FinanceProfitAbilityQueryParams(QueryParams):
    """财务指标-盈利能力"""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))


class FinanceProfitAbilityData(Data):
    """财务指标-盈利能力"""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company.")
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get(
            "timestamp", "Reporting period publication time."
        )
    )
