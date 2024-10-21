from typing import Any, Dict, List, Optional

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher

from openbb_xiaoyuan.standard_models.du_pont_analysis import DuPontAnalysisQueryParams, DuPontAnalysisData

reader = get_jindata_reader()


class XYDuPontAnalysisQueryParams(DuPontAnalysisQueryParams):
    pass


class XYDuPontAnalysisData(DuPontAnalysisData):
    """权益乘数（杜邦分析）"""
    # __alias_dict__ = {"权益乘数（杜邦分析）": "权益乘数（杜邦分析）"}
    pass

class XYDuPontAnalysisFetcher(
    Fetcher[
        XYDuPontAnalysisQueryParams,
        List[XYDuPontAnalysisData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XYDuPontAnalysisQueryParams:
        return XYDuPontAnalysisQueryParams(**params)

    @staticmethod
    def extract_data(
            query: XYDuPontAnalysisQueryParams,
            credentials: Optional[Dict[str, str]],
            **kwargs: Any,
    ) -> List[dict]:
        symbols = query.symbol.split(",")
        start_date = reader.convert_to_db_date_format(query.start_date)
        end_date = reader.convert_to_db_date_format(query.end_date)
        df = reader.get_finance_factors(
            source="1Y",
            frequency="1Q",
            factor_names=[
                "权益乘数（杜邦分析）",
            ],
            start_date=start_date,
            end_date=end_date,
            symbols=symbols,
        )

        data = df.to_dict(orient='records')
        return data

    @staticmethod
    def transform_data(
            query: XYDuPontAnalysisQueryParams, data: List[dict], **kwargs: Any
    ) -> List[XYDuPontAnalysisData]:
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')
        return [XYDuPontAnalysisData(**d) for d in data]
