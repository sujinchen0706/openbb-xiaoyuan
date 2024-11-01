"""XiaoYuan Finance Metrics Per Share Model."""

from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field

from openbb_xiaoyuan.standard_models.financial_metrics_per_share import (
    PerShareIndicatorQueryParams,
    PerShareIndicatorData,
)
from openbb_xiaoyuan.utils.references import (
    extractMonthDayFromTime,
    get_query_finance_sql,
    get_report_month,
)


class XiaoYuanPerShareIndicatorQueryParams(PerShareIndicatorQueryParams):
    """XiaoYuan Per Share Indicator Query."""

    __json_schema_extra__ = {
        "period": {
            "choices": ["fy", "q1", "q2ytd", "q3ytd", "annual"],
        }
    }

    period: Literal["fy", "q1", "q2ytd", "q3ytd", "annual"] = Field(
        default="fy",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )

    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class XiaoYuanPerShareIndicatorData(PerShareIndicatorData):
    """XiaoYuan Finance Cash Flow Statement Data."""

    __alias_dict__ = {
        "period_ending": "报告期",
        "eps_diluted": "期末摊薄每股收益（元）",
        "eps_excl_extraordinary": "扣非每股收益（元）",
        "eps_ttm": "每股收益EPSTTM（元）",
        "nav_per_share": "每股净资产（元）",
        "total_revenue_per_share": "每股营业总收入（元）",
        "revenue_per_share": "每股营业收入（元）",
        "revenue_p_share_ttm": "每股营业收入TTM（元）",
        "ebit_per_share": "每股息税前利润（元）",
        "capital_reserve_per_share": "每股资本公积（元）",
        "surplus_reserve_per_share": "每股盈余公积（元）",
        "undistributed_profit_per_share": "每股未分配利润（元）",
        "retained_earnings_per_share": "每股留存收益（元）",
        "ocf_per_share": "每股经营活动产生的现金流量净额（元）",
        "ocf_p_share_ttm": "每股经营活动产生的现金流量净额TTM（元）",
        "ncf_per_share": "每股现金流量净额（元）",
        "ncf_p_share_ttm": "每股现金流量净额TTM（元）",
        "fcf_to_firm_per_share": "每股企业自由现金流量（元）",
        "fcf_to_equity_per_share": "每股股东自由现金流量（元）",
    }


class XiaoYuanPerShareIndicatorFetcher(
    Fetcher[
        XiaoYuanPerShareIndicatorQueryParams,
        List[XiaoYuanPerShareIndicatorData],
    ]
):
    """Extract the data from the XiaoYuan Finance endpoints."""

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
        """Extract the data from the XiaoYuan Finance endpoints."""
        from jinniuai_data_store.reader import get_jindata_reader

        reader = get_jindata_reader()
        FIN_METRICS_PER_SHARE = [
            "期末摊薄每股收益（元）",
            "扣非每股收益（元）",
            "每股收益EPSTTM（元）",
            "每股净资产（元）",
            "每股营业总收入（元）",
            "每股营业收入（元）",
            "每股营业收入TTM（元）",
            "每股息税前利润（元）",
            "每股资本公积（元）",
            "每股盈余公积（元）",
            "每股未分配利润（元）",
            "每股留存收益（元）",
            "每股经营活动产生的现金流量净额（元）",
            "每股经营活动产生的现金流量净额TTM（元）",
            "每股现金流量净额（元）",
            "每股现金流量净额TTM（元）",
            "每股企业自由现金流量（元）",
            "每股股东自由现金流量（元）",
        ]
        report_month = get_report_month(query.period)
        finance_sql = get_query_finance_sql(
            FIN_METRICS_PER_SHARE, [query.symbol], report_month
        )
        df = reader._run_query(
            script=extractMonthDayFromTime + finance_sql,
        )
        if df is None or df.empty:
            raise EmptyDataError()
        df["报告期"] = df["报告期"].dt.strftime("%Y-%m-%d")
        df.sort_values(by="报告期", ascending=False, inplace=True)
        data = df.to_dict(orient="records")

        return data

    @staticmethod
    def transform_data(
        # pylint: disable=unused-argument
        query: XiaoYuanPerShareIndicatorQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[XiaoYuanPerShareIndicatorData]:
        """Transform the data."""
        return [XiaoYuanPerShareIndicatorData.model_validate(d) for d in data]
