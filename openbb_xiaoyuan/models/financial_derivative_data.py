from typing import Any, Dict, List, Optional

import pandas as pd

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher

from openbb_xiaoyuan.standard_models.financial_derivative_data import FinancialDerivativeQueryParams, \
    FinancialDerivativeData

reader = get_jindata_reader()

class XYFinancialDerivativeQueryParams(FinancialDerivativeQueryParams):
    pass


class XYFinancialDerivativeData(FinancialDerivativeData):
    pass


class XYFinancialDerivativeFetcher(
    Fetcher[
        XYFinancialDerivativeQueryParams,
        List[XYFinancialDerivativeData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XYFinancialDerivativeQueryParams:
        return XYFinancialDerivativeQueryParams(**params)

    @staticmethod
    def extract_data(
            query: XYFinancialDerivativeQueryParams,
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
                "无息流动负债",
                "无息非流动负债",
                "带息债务",
                "净债务",
                "有形净资产",
                "营运资本",
                "净营运资本",
                "留存收益",
                "毛利",
                "经营活动净收益",
                "价值变动净收益",
                "息税前利润",
                "息税折旧摊销前利润",
                "非经常性损益",
                "扣除非经常性损益后的归属于上市公司股东的净利润",
                "企业自由现金流量",
                "股权自由现金流量",
                "折旧与摊销",
            ],
            start_date=start_date,
            end_date=end_date,
            symbols=symbols,
        )

        data = df.to_dict(orient='records')
        return data

    @staticmethod
    def transform_data(
            query: XYFinancialDerivativeQueryParams, data: List[dict], **kwargs: Any
    ) -> List[XYFinancialDerivativeData]:
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')
        return [XYFinancialDerivativeData(**d) for d in data]
