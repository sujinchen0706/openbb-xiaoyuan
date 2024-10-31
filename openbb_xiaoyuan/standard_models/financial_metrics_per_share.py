"""Financial Metrics - Per Share Standard Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS


class PerShareIndicatorQueryParams(QueryParams):
    """Per Share Indicator Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class PerShareIndicatorData(Data):
    """Per Share Indicator Data."""

    period_ending: Optional[dateType] = Field(
        description="The end date of the reporting period."
    )
