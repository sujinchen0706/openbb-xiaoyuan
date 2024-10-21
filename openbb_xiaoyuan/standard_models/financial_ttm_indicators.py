"""财务TTM指标"""
from datetime import date as dateType
from typing import Optional, Union

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class FinancialTTMIndicatorsQueryParams(QueryParams):
    """财务TTM指标"""
    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", []))
    start_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: str = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class FinancialTTMIndicatorsData(Data):
    """财务TTM指标"""
    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company.")
    )
    timestamp: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("timestamp", "日期")
    )
    报告期: Optional[dateType] = Field(
        description=DATA_DESCRIPTIONS.get("报告期", "报告期")
    )
    营业总收入TTM: float = Field(description=DATA_DESCRIPTIONS.get("营业总收入TTM","营业总收入TTM"))
    营业总成本TTM: float = Field(description=DATA_DESCRIPTIONS.get("营业总成本TTM","营业总成本TTM"))
    营业收入TTM: float = Field(description=DATA_DESCRIPTIONS.get("营业收入TTM","营业收入TTM"))
    营业成本非金融类TTM: float = Field(description=DATA_DESCRIPTIONS.get("营业成本非金融类TTM","营业成本非金融类TTM"))
    营业支出金融类TTM: float = Field(description=DATA_DESCRIPTIONS.get("营业支出金融类TTM","营业支出金融类TTM"))
    毛利TTM: float = Field(description=DATA_DESCRIPTIONS.get("毛利TTM","毛利TTM"))
    销售费用TTM: float = Field(description=DATA_DESCRIPTIONS.get("销售费用TTM","销售费用TTM"))
    管理费用TTM: float = Field(description=DATA_DESCRIPTIONS.get("管理费用TTM","管理费用TTM"))
    财务费用TTM: float = Field(description=DATA_DESCRIPTIONS.get("财务费用TTM","财务费用TTM"))
    资产减值损失TTM: float = Field(description=DATA_DESCRIPTIONS.get("资产减值损失TTM","资产减值损失TTM"))
    经营活动净收益TTM: float = Field(description=DATA_DESCRIPTIONS.get("经营活动净收益TTM","经营活动净收益TTM"))
    价值变动净收益TTM: float = Field(description=DATA_DESCRIPTIONS.get("价值变动净收益TTM","价值变动净收益TTM"))
    营业利润TTM: float = Field(description=DATA_DESCRIPTIONS.get("营业利润TTM","营业利润TTM"))
    营业外收支净额TTM: float = Field(description=DATA_DESCRIPTIONS.get("营业外收支净额TTM","营业外收支净额TTM"))
    息税前利润TTM: float = Field(description=DATA_DESCRIPTIONS.get("息税前利润TTM","息税前利润TTM"))
    利润总额TTM: float = Field(description=DATA_DESCRIPTIONS.get("利润总额TTM","利润总额TTM"))
    所得税TTM: float = Field(description=DATA_DESCRIPTIONS.get("所得税TTM","所得税TTM"))
    归属母公司股东的净利润TTM: float = Field(description=DATA_DESCRIPTIONS.get("归属母公司股东的净利润TTM","归属母公司股东的净利润TTM"))
