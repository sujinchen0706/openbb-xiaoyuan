from typing import Any, Dict, List, Optional

import pandas as pd
from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher

from openbb_xiaoyuan.standard_models.calculate_reduction_percentage import (
    CalculateReductionPercentageQueryParams,
    CalculateReductionPercentageData,
)


class XiaoYuanCalculateReductionPercentageQueryParams(
    CalculateReductionPercentageQueryParams
):
    """XiaoYuan Calculate Reduction Percentage Query."""

    __json_schema_extra__ = {
        "symbol": {"multiple_items_allowed": True},
    }

    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class XiaoYuanCalculateReductionPercentageData(CalculateReductionPercentageData):
    """XiaoYuan Calculate Reduction Percentage Data."""

    __alias_dict__ = {"calculate_reduction_percentage": "过去一年董监高合计减持比例"}


class XiaoYuanCalculateReductionPercentageFetcher(
    Fetcher[
        XiaoYuanCalculateReductionPercentageQueryParams,
        List[XiaoYuanCalculateReductionPercentageData],
    ]
):
    """Transform the query, extract and transform the data from the XiaoYuan endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> XiaoYuanCalculateReductionPercentageQueryParams:
        """Transform the query parameters."""
        return XiaoYuanCalculateReductionPercentageQueryParams(**params)

    @staticmethod
    def extract_data(
        query: XiaoYuanCalculateReductionPercentageQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Extract data from the data source."""
        reader = get_jindata_reader()
        symbols = query.symbol.split(",")

        start_date = query.start_date
        end_date = query.end_date
        df = reader.get_factors(
            source="6M",
            frequency="1D",
            factor_names=["过去一年董监高合计减持比例"],
            start_date=start_date,
            end_date=end_date,
            symbols=symbols,
        )
        df = df.sort_values(by="timestamp", ascending=False)
        data = df.to_dict(orient="records")
        return data

    @staticmethod
    def transform_data(
        query: XiaoYuanCalculateReductionPercentageQueryParams,
        data: List[dict],
        **kwargs: Any,
    ) -> List[XiaoYuanCalculateReductionPercentageData]:
        """Transform the raw data into structured data."""
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient="records")
        return [
            XiaoYuanCalculateReductionPercentageData.model_validate(d) for d in data
        ]
