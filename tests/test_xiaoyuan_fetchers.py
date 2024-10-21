"""Tests for XiaoYuan fetchers."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_xiaoyuan.models.financial_metrics_per_share import (
    XiaoYuanPerShareIndicatorFetcher,
)

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
def test_xiaoyuan_per_share_indicator_fetcher(credentials=test_credentials):
    """Test XiaoYuanPerShareIndicatorFetcher."""
    # ["fy", "q1", "q2ytd", "q3ytd", "annual"]
    params = {"symbol": "SH600519", "period": "annual"}

    fetcher = XiaoYuanPerShareIndicatorFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
