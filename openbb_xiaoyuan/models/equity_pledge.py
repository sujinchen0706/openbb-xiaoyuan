"""XiaoYuan Equity Pledge Model."""

from typing import Any, Dict, List, Optional

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher

from openbb_xiaoyuan.standard_models.equity_pledge import (
    EquityPledgeQueryParams,
    EquityPledgeData,
)

reader = get_jindata_reader()


class XiaoYuanEquityPledgeQueryParams(EquityPledgeQueryParams):
    """XiaoYuan Equity Pledge Query."""

    ...


class XiaoYuanEquityPledgeData(EquityPledgeData):
    """XiaoYuan Equity Pledge Data."""

    __alias_dict__ = {"stock_pledge_ratio": "股票质押率"}


class XiaoYuanEquityPledgeFetcher(
    Fetcher[
        XiaoYuanEquityPledgeQueryParams,
        List[XiaoYuanEquityPledgeData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XiaoYuanEquityPledgeQueryParams:
        return XiaoYuanEquityPledgeQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanEquityPledgeQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data from the data source."""
        symbols = query.symbol.split(",")
        start_date = reader.convert_to_db_date_format(query.start_date)
        end_date = reader.convert_to_db_date_format(query.end_date)
        df = reader.get_factors(
            source="6M",
            frequency="1D",
            factor_names=["股票质押率"],
            start_date=start_date,
            end_date=end_date,
            symbols=symbols,
        )
        df = df.sort_values(by="timestamp", ascending=False)
        data = df.to_dict(orient="records")
        return data

    @staticmethod
    def transform_data(
        # pylint: disable=unused-argument
        query: XiaoYuanEquityPledgeQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanEquityPledgeData]:
        """Transform the data."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [XiaoYuanEquityPledgeData.model_validate(d) for d in data]
