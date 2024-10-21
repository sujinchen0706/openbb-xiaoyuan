import pytest
from openbb_core.app.service.user_service import UserService

from openbb_xiaoyuan.models.calculate_reduction_percentage import (
    XYCalculateReductionPercentageFetcher,
)
from openbb_xiaoyuan.models.enterprise_life_cycle import XYEnterpriseLifeCycleFetcher
from openbb_xiaoyuan.models.financial_derivative_data import (
    XYFinancialDerivativeFetcher,
)
from openbb_xiaoyuan.models.financial_ttm_indicators import (
    XYFinancialTTMIndicatorsFetcher,
)
from openbb_xiaoyuan.models.st_name import XYStNameFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.mark.vcr()
def test_xy_enterprise_life_cycle_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,APPL",
        "start_date": "2021-01-01",
        "end_date": "2023-12-31",
    }

    fetcher = XYEnterpriseLifeCycleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.vcr()
def test_xy_enterprise_life_cycle_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,APPL",
        "start_date": "2021-01-01",
        "end_date": "2023-12-31",
    }

    fetcher = XYCalculateReductionPercentageFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.vcr()
def test_xy_st_name_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "start_date": "2021-01-01",
        "end_date": "2023-12-31",
    }

    fetcher = XYStNameFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.vcr()
def test_xy_financial_derivative_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "start_date": "2021-01-01",
        "end_date": "2023-12-31",
    }

    fetcher = XYFinancialDerivativeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


def test_xy_financial_ttm_indicators_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "start_date": "2021-01-01",
        "end_date": "2023-12-31",
    }

    fetcher = XYFinancialTTMIndicatorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
