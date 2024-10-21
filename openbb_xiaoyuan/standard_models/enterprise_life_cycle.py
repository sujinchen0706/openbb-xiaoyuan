"""企业生命周期"""

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


class EnterpriseLifeCycleQueryParams(QueryParams):
    """企业生命周期查询参数"""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", []))
    start_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class EnterpriseLifeCycleData(Data):
    """企业生命周期数据"""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company.")
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("timestamp", "日期")
    )
    报告期: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("报告期", "报告期")
    )
    企业生命周期: float = Field(
        description=DATA_DESCRIPTIONS.get("企业生命周期", "企业生命周期")
    )
