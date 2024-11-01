"""Tests for XiaoYuan fetchers."""

import pytest
from openbb_core.app.service.user_service import UserService

from openbb_xiaoyuan.models.balance_sheet import XiaoYuanBalanceSheetFetcher
from openbb_xiaoyuan.models.cash_flow import XiaoYuanCashFlowStatementFetcher
from openbb_xiaoyuan.models.cash_flow_growth import (
    XiaoYuanCashFlowStatementGrowthFetcher,
)
from openbb_xiaoyuan.models.financial_ratios import (
    XiaoYuanFinancialRatiosFetcher,
)
from openbb_xiaoyuan.models.balance_sheet_growth import (
    XiaoYuanBalanceSheetGrowthFetcher,
)
from openbb_xiaoyuan.models.income_statement_growth import (
    XiaoYuanIncomeStatementGrowthFetcher,
)
from openbb_xiaoyuan.models.income_statement import XiaoYuanIncomeStatementFetcher
from openbb_xiaoyuan.models.key_metrics import XiaoYuanKeyMetricsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Cookie", "MOCK_COOKIE"),
            ("crumb", "MOCK_CRUMB"),
        ],
        "filter_query_parameters": [
            ("period1", "MOCK_PERIOD_1"),
            ("period2", "MOCK_PERIOD_2"),
            ("crumb", "MOCK_CRUMB"),
            ("date", "MOCK_DATE"),
        ],
    }


@pytest.mark.record_http
def test_xiaoyuan_financial_ratios_fetcher(credentials=test_credentials):
    """Test XiaoYuanFinancialRatiosFetcher."""
    params = {"symbol": "SH600519", "period": "annual", "limit": 4}
    fetcher = XiaoYuanFinancialRatiosFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xiaoyuan_cash_growth_fetcher(credentials=test_credentials):
    """Test XiaoYuanCashFlowStatementGrowthFetcher."""
    params = {"symbol": "SH600519", "period": "annual", "limit": 4}
    fetcher = XiaoYuanCashFlowStatementGrowthFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xiaoyuan_balance_growth_fetcher(credentials=test_credentials):
    """Test XiaoYuanBalanceSheetGrowthFetcher."""
    params = {"symbol": "SH600519", "period": "annual", "limit": 4}
    fetcher = XiaoYuanBalanceSheetGrowthFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xiaoyuan_cash_flow_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }

    fetcher = XiaoYuanCashFlowStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# @pytest.mark.record_http
def test_xiaoyuan_balance_sheet_fetcher(credentials=test_credentials):
    """Test XiaoYuanPerShareIndicatorFetcher."""
    # ["fy", "q1", "q2ytd", "q3ytd", "annual"]
    params = {"symbol": "SH600519", "period": "ytd"}

    fetcher = XiaoYuanBalanceSheetFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xiaoyuan_income_statement_fetcher(credentials=test_credentials):
    """Test XiaoYuanIncomeStatementFetcher."""
    # ["ytd", "annual"]
    params = {"symbol": "SH600519", "period": "ytd"}

    fetcher = XiaoYuanIncomeStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# @pytest.mark.record_http
def test_xiaoyuan_key_metrics_fetcher(credentials=test_credentials):
    """Test XiaoYuanKeyMetricsFetcher."""
    # ["ytd", "annual"]
    params = {"symbol": "SH600519", "period": "ytd"}

    fetcher = XiaoYuanKeyMetricsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xiao_yuan_income_statement_growth_fetcher(credentials=test_credentials):
    """Test XiaoYuanIncomeStatementGrowthFetcher."""
    params = {"symbol": "SH600519", "period": "annual", "limit": 4}
    fetcher = XiaoYuanIncomeStatementGrowthFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
