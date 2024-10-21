from typing import Any, Dict, List, Optional

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher

from openbb_xiaoyuan.standard_models.financial_ttm_indicators import FinancialTTMIndicatorsQueryParams, \
    FinancialTTMIndicatorsData

reader = get_jindata_reader()

class XYFinancialTTMIndicatorsQueryParams(FinancialTTMIndicatorsQueryParams):
    pass


class XYFinancialTTMIndicatorsData(FinancialTTMIndicatorsData):
    pass


class XYFinancialTTMIndicatorsFetcher(
    Fetcher[
        XYFinancialTTMIndicatorsQueryParams,
        List[XYFinancialTTMIndicatorsData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XYFinancialTTMIndicatorsQueryParams:
        return XYFinancialTTMIndicatorsQueryParams(**params)

    @staticmethod
    def extract_data(
            query: XYFinancialTTMIndicatorsQueryParams,
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
                "营业总收入TTM",
                "营业总成本TTM",
                "营业收入TTM",
                "营业成本非金融类TTM",
                "营业支出金融类TTM",
                "毛利TTM",
                "销售费用TTM",
                "管理费用TTM",
                "财务费用TTM",
                "资产减值损失TTM",
                "经营活动净收益TTM",
                "价值变动净收益TTM",
                "营业利润TTM",
                "营业外收支净额TTM",
                "息税前利润TTM",
                "利润总额TTM",
                "所得税TTM",
                "归属母公司股东的净利润TTM",
            ],
            start_date=start_date,
            end_date=end_date,
            symbols=symbols,
        )

        data = df.to_dict(orient='records')
        return data

    @staticmethod
    def transform_data(
            query: XYFinancialTTMIndicatorsQueryParams, data: List[dict], **kwargs: Any
    ) -> List[XYFinancialTTMIndicatorsData]:
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')
        return [XYFinancialTTMIndicatorsData(**d) for d in data]
