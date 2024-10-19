"""Yahoo Finance Cash Flow Statement Model."""

import json
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cash_flow import (
    CashFlowStatementData,
    CashFlowStatementQueryParams
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import to_snake_case
from pydantic import Field, field_validator

from openbb_xiaoyuan.standard_models.financial_metrics_per_share import PerShareIndicatorQueryParams, \
    PerShareIndicatorData


class XiaoYuanPerShareIndicatorQueryParams(PerShareIndicatorQueryParams):
    """小原 财务指标-每股 指标查询.

    Source:
    """

    __json_schema_extra__ = {
        "period": {
            "choices": ["annual", "quarter"],
        }
    }

    period: Literal["annual", "quarter"] = Field(
        default="annual",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )


class XiaoYuanPerShareIndicatorData(CashFlowStatementData):
    """Yahoo Finance Cash Flow Statement Data."""

    __alias_dict__ = {
        'eps_diluted': '期末摊薄每股收益（元）',
        'eps_excl_extraordinary': '扣非每股收益（元）',
        'eps_ttm': '每股收益EPSTTM（元）',
        'nav_per_share': '每股净资产（元）',
        'total_revenue_per_share': '每股营业总收入（元）',
        'revenue_per_share': '每股营业收入（元）',
        'revenue_p_share_ttm': '每股营业收入TTM（元）',
        'ebit_per_share': '每股息税前利润（元）',
        'capital_reserve_per_share': '每股资本公积（元）',
        'surplus_reserve_per_share': '每股盈余公积（元）',
        'undistributed_profit_per_share': '每股未分配利润（元）',
        'retained_earnings_per_share': '每股留存收益（元）',
        'ocf_per_share': '每股经营活动产生的现金流量净额（元）',
        'ocf_p_share_ttm': '每股经营活动产生的现金流量净额TTM（元）',
        'ncf_per_share': '每股现金流量净额（元）',
        'ncf_p_share_ttm': '每股现金流量净额TTM（元）',
        'fcf_to_firm_per_share': '每股企业自由现金流量（元）',
        'fcf_to_equity_per_share': '每股股东自由现金流量（元）'
    }

    @field_validator("period_ending", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return datetime object from string."""
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S").date()
        return v


class XiaoYuanPerShareIndicatorFetcher(
    Fetcher[
        XiaoYuanPerShareIndicatorQueryParams,
        List[PerShareIndicatorData],
    ]
):
    """转换查询，提取并转换来自小原的数据。"""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XiaoYuanPerShareIndicatorQueryParams:
        """Transform the query parameters."""
        return XiaoYuanPerShareIndicatorQueryParams(**params)

    @staticmethod
    def extract_data(
            # pylint: disable=unused-argument
            query: XiaoYuanPerShareIndicatorQueryParams,
            credentials: Optional[Dict[str, str]],
            **kwargs: Any,
    ) -> List[PerShareIndicatorData]:
        """Extract the data from the Yahoo Finance endpoints."""
        from yfinance import Ticker  # pylint: disable=import-outside-toplevel
        from jinniuai_data_store.reader import get_jindata_reader
        reader = get_jindata_reader()
        period = "yearly" if query.period == "annual" else "quarterly"  # type: ignore
        # data = Ticker(query.symbol).get_cash_flow(
        #     as_dict=False, pretty=False, freq=period
        # )
        factor_names = ['期末摊薄每股收益（元）',
                        '扣非每股收益（元）',
                        '每股收益EPSTTM（元）',
                        '每股净资产（元）',
                        '每股营业总收入（元）',
                        '每股营业收入（元）',
                        '每股营业收入TTM（元）',
                        '每股息税前利润（元）',
                        '每股资本公积（元）',
                        '每股盈余公积（元）',
                        '每股未分配利润（元）',
                        '每股留存收益（元）',
                        '每股经营活动产生的现金流量净额（元）',
                        '每股经营活动产生的现金流量净额TTM（元）',
                        '每股现金流量净额（元）',
                        '每股现金流量净额TTM（元）',
                        '每股企业自由现金流量（元）',
                        '每股股东自由现金流量（元）']
        script = f"""

              //获取财务数据
              t = select 报告期, symbol, factor_name ,value
                  from loadTable("dfs://finance_factors_1Y", `cn_finance_factors_1Q)
                  where factor_name in {factor_names} 
                  and symbol in {[query.symbol]} 
                  context by symbol,factor_name, groupByTime(报告期)  order by 报告期 limit -4;
              select value from t pivot by 报告期, symbol, factor_name;
              """
        data = reader._run_query(
        )

        if data is None:
            raise EmptyDataError()

        data.index = [to_snake_case(i) for i in data.index]
        data = data.reset_index().sort_index(ascending=False).set_index("index")
        data = data.fillna("N/A").replace("N/A", None).to_dict()
        data = [{"period_ending": str(key), **value} for key, value in data.items()]

        data = json.loads(json.dumps(data))

        return data

    @staticmethod
    def transform_data(
            # pylint: disable=unused-argument
            query: XiaoYuanPerShareIndicatorQueryParams,
            data: List[Dict],
            **kwargs: Any,
    ) -> List[PerShareIndicatorData]:
        """Transform the data."""
        return [PerShareIndicatorData.model_validate(d) for d in data]
