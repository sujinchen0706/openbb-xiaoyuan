from typing import Any, Dict, List, Optional

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from pydantic import Field
from openbb_xiaoyuan.standard_models.enterprise_life_cycle import (
    EnterpriseLifeCycleQueryParams,
    EnterpriseLifeCycleData,
)

reader = get_jindata_reader()


class XYEnterpriseLifeCycleQueryParams(EnterpriseLifeCycleQueryParams):
    symbol: str = Field(description="Symbol to query.")


class XYEnterpriseLifeCycleData(EnterpriseLifeCycleData):
    """House Disclosure Data Model."""

    # __alias_dict__ = {"symbol": "ticker"}
    pass


class ExampleData(Data):
    """Sample provider data.

    The fields are displayed as-is in the output of the command. In this case, its the
    Open, High, Low, Close and Volume data.
    """

    o: float = Field(description="Open price.")
    h: float = Field(description="High price.")
    l: float = Field(description="Low price.")
    c: float = Field(description="Close price.")
    v: float = Field(description="Volume.")
    d: str = Field(description="Date")


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
        """Return the raw data from the House Disclosure endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")
        results: List[Dict] = []
        df = reader.get_symbols(symbols)

        return results

    @staticmethod
    def transform_data(
        query: XYEnterpriseLifeCycleQueryParams, data: List[dict], **kwargs: Any
    ) -> List[XYEnterpriseLifeCycleData]:
        return [XYEnterpriseLifeCycleData(**d) for d in data]
