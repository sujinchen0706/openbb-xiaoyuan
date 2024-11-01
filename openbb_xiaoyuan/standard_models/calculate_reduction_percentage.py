"""Calculate Reduction Percentage Standard Model."""

from datetime import date as dateType
from typing import Optional

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class ReductionPercentageQueryParams(QueryParams):
    """Total reduction percentage of directors and senior executives over the past yea"""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class ReductionPercentageData(Data):
    """Total reduction percentage of directors and senior executives over the past yea"""

    symbol: str = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company."),
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("timestamp", "The date.")
    )
