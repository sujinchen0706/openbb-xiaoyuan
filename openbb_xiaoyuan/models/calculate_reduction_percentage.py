from typing import Any, Dict, List, Optional

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader

from openbb_core.provider.abstract.fetcher import Fetcher

from openbb_xiaoyuan.standard_models.calculate_reduction_percentage import CalculateReductionPercentageQueryParams, \
    CalculateReductionPercentageData

reader = get_jindata_reader()


class XYCalculateReductionPercentageQueryParams(CalculateReductionPercentageQueryParams):
    pass


class XYCalculateReductionPercentageData(CalculateReductionPercentageData):
    pass


class XYCalculateReductionPercentageFetcher(
    Fetcher[
        XYCalculateReductionPercentageQueryParams,
        List[XYCalculateReductionPercentageData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XYCalculateReductionPercentageQueryParams:
        return XYCalculateReductionPercentageQueryParams(**params)

    @staticmethod
    def extract_data(
            query: XYCalculateReductionPercentageQueryParams,
            credentials: Optional[Dict[str, str]],
            **kwargs: Any,
    ) -> List[dict]:
        symbols = query.symbol.split(",")
        start_date = reader.convert_to_db_date_format(query.start_date)
        end_date = reader.convert_to_db_date_format(query.end_date)
        df = reader.get_factors(
            source="6M",
            frequency="1D",
            factor_names=["过去一年董监高合计减持比例"],
            start_date=start_date,
            end_date=end_date,
            symbols=symbols,
        )

        data = df.to_dict(orient='records')
        return data

    @staticmethod
    def transform_data(
            query: XYCalculateReductionPercentageQueryParams, data: List[dict], **kwargs: Any
    ) -> List[XYCalculateReductionPercentageData]:
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')
        return [XYCalculateReductionPercentageData(**d) for d in data]
