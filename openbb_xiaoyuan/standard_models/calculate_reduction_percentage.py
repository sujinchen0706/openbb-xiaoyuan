"""过去一年董监高合计减持比例"""
import datetime
from datetime import date as dateType
from typing import Optional, Union

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator

class CalculateReductionPercentageQueryParams(QueryParams):
    """过去一年董监高合计减持比例"""
    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", []))
    start_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )

class CalculateReductionPercentageData(Data):
    """过去一年董监高合计减持比例"""
    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company.")
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("timestamp", "日期")
    )
    过去一年董监高合计减持比例: float = Field(
        description=DATA_DESCRIPTIONS.get("过去一年董监高合计减持比例", "过去一年董监高合计减持比例")
    )
