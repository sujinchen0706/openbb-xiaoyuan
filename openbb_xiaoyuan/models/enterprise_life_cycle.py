from typing import Any, Dict, List, Optional

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_xiaoyuan.standard_models.enterprise_life_cycle import EnterpriseLifeCycleQueryParams, \
    EnterpriseLifeCycleData

reader = get_jindata_reader()
class XYEnterpriseLifeCycleQueryParams(EnterpriseLifeCycleQueryParams):
    pass


class XYEnterpriseLifeCycleData(EnterpriseLifeCycleData):
    pass


class XYEnterpriseLifeCycleFetcher(
    Fetcher[
        XYEnterpriseLifeCycleQueryParams,
        List[XYEnterpriseLifeCycleData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XYEnterpriseLifeCycleQueryParams:
        return XYEnterpriseLifeCycleQueryParams(**params)

    @staticmethod
    def extract_data(
            query: XYEnterpriseLifeCycleQueryParams,
            credentials: Optional[Dict[str, str]],
            **kwargs: Any,
    ) -> List[dict]:
        symbols = query.symbol.split(",")
        start_date = reader.convert_to_db_date_format(query.start_date)
        end_date = reader.convert_to_db_date_format(query.end_date)
        df = reader.get_finance_factors(
            source="1Y",
            frequency="1Y",
            factor_names=[
                "企业生命周期",
            ],
            start_date=start_date,
            end_date=end_date,
            symbols=symbols,
        )

        data = df.to_dict(orient='records')
        return data

    @staticmethod
    def transform_data(
            query: XYEnterpriseLifeCycleQueryParams, data: List[dict], **kwargs: Any
    ) -> List[XYEnterpriseLifeCycleData]:
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')
        return [XYEnterpriseLifeCycleData(**d) for d in data]
