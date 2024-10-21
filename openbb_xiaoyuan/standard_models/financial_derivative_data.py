"""企业生命周期"""

from datetime import date as dateType
from typing import Optional, Union

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class FinancialDerivativeQueryParams(QueryParams):
    """财务衍生数据"""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", []))
    start_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class FinancialDerivativeData(Data):
    """财务衍生数据"""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company.")
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("timestamp", "日期")
    )
    报告期: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("报告期", "报告期")
    )
    无息流动负债: float = Field(
        description=DATA_DESCRIPTIONS.get("无息流动负债", "无息流动负债")
    )
    无息非流动负债: float = Field(
        description=DATA_DESCRIPTIONS.get("无息非流动负债", "无息非流动负债")
    )
    带息债务: float = Field(description=DATA_DESCRIPTIONS.get("带息债务", "带息债务"))
    净债务: float = Field(description=DATA_DESCRIPTIONS.get("净债务", "净债务"))
    有形净资产: float = Field(
        description=DATA_DESCRIPTIONS.get("有形净资产", "有形净资产")
    )
    营运资本: float = Field(description=DATA_DESCRIPTIONS.get("营运资本", "营运资本"))
    净营运资本: float = Field(
        description=DATA_DESCRIPTIONS.get("净营运资本", "净营运资本")
    )
    留存收益: float = Field(description=DATA_DESCRIPTIONS.get("留存收益", "留存收益"))
    毛利: float = Field(description=DATA_DESCRIPTIONS.get("毛利", "毛利"))
    经营活动净收益: float = Field(
        description=DATA_DESCRIPTIONS.get("经营活动净收益", "经营活动净收益")
    )
    价值变动净收益: float = Field(
        description=DATA_DESCRIPTIONS.get("价值变动净收益", "价值变动净收益")
    )
    息税前利润: float = Field(
        description=DATA_DESCRIPTIONS.get("息税前利润", "息税前利润")
    )
    息税折旧摊销前利润: float = Field(
        description=DATA_DESCRIPTIONS.get("息税折旧摊销前利润", "息税折旧摊销前利润")
    )
    非经常性损益: float = Field(
        description=DATA_DESCRIPTIONS.get("非经常性损益", "非经常性损益")
    )
    扣除非经常性损益后的归属于上市公司股东的净利润: float = Field(
        description=DATA_DESCRIPTIONS.get(
            "扣除非经常性损益后的归属于上市公司股东的净利润",
            "扣除非经常性损益后的归属于上市公司股东的净利润",
        )
    )
    企业自由现金流量: float = Field(
        description=DATA_DESCRIPTIONS.get("企业自由现金流量", "企业自由现金流量")
    )
    股权自由现金流量: float = Field(
        description=DATA_DESCRIPTIONS.get("股权自由现金流量", "股权自由现金流量")
    )
    折旧与摊销: float = Field(
        description=DATA_DESCRIPTIONS.get("折旧与摊销", "折旧与摊销")
    )
