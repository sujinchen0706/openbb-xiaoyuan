"""Finance Indicator - Debt-Paying Ability Standard Model."""

from typing import Optional
from datetime import date as dateType
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class FinanceDebtpayingAbilityQueryParams(QueryParams):
    """Finance Indicator - Debt-Paying Ability Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))


class FinanceDebtpayingAbilityData(Data):
    """Finance Indicator - Debt-Paying Ability Data."""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company.")
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get(
            "timestamp", "Reporting period publication time."
        )
    )
    period_ending: Optional[dateType] = Field(
        description="The end date of the reporting period."
    )
