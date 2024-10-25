from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService

from openbb_xiaoyuan.models.calculate_reduction_percentage import (
    XiaoYuanCalculateReductionPercentageFetcher,
)
from openbb_xiaoyuan.models.cash_flow import XiaoYuanCashFlowStatementFetcher
from openbb_xiaoyuan.models.du_pont_analysis import XiaoYuanDuPontAnalysisFetcher
from openbb_xiaoyuan.models.enterprise_life_cycle import (
    XiaoYuanEnterpriseLifeCycleFetcher,
)
from openbb_xiaoyuan.models.equity_pledge import XiaoYuanEquityPledgeFetcher
from openbb_xiaoyuan.models.finance_capital_structure import (
    XiaoYuanFinanceCapitalStructureFetcher,
)
from openbb_xiaoyuan.models.finance_cash_position import (
    XiaoYuanFinanceCashpositionFetcher,
)
from openbb_xiaoyuan.models.finance_operational_capability import (
    XiaoYuanFinanceOperationalCapabilityFetcher,
)
from openbb_xiaoyuan.models.finance_profit_ability import (
    XiaoYuanFinanceProfitAbilityFetcher,
)
from openbb_xiaoyuan.models.finance_revenue_quality import (
    XiaoYuanFinanceRevenueQualityFetcher,
)
from openbb_xiaoyuan.models.financial_derivative_data import (
    XiaoYuanFinancialDerivativeFetcher,
)
from openbb_xiaoyuan.models.financial_metrics_per_share import (
    XiaoYuanPerShareIndicatorFetcher,
)
from openbb_xiaoyuan.models.financial_ttm_indicators import (
    XiaoYuanFinancialTTMIndicatorsFetcher,
)
from openbb_xiaoyuan.models.st_name import XiaoYuanStNameFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.mark.record_http
def test_xy_enterprise_life_cycle_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,APPL",
        "period": "annual",
    }

    fetcher = XiaoYuanEnterpriseLifeCycleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_calculate_reduction_percentage_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519",
        "start_date": date(2021, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = XiaoYuanCalculateReductionPercentageFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_du_pont_analysis_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415",
        "period": "annual",
    }

    fetcher = XiaoYuanDuPontAnalysisFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# @pytest.mark.record_http
def test_xy_st_name_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "start_date": date(2021, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = XiaoYuanStNameFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_financial_derivative_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }

    fetcher = XiaoYuanFinancialDerivativeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_financial_ttm_indicators_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }

    fetcher = XiaoYuanFinancialTTMIndicatorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_finance_profit_ability_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }

    fetcher = XiaoYuanFinanceProfitAbilityFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_cash_flow_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }

    fetcher = XiaoYuanCashFlowStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_finance_operational_capability_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }
    fetcher = XiaoYuanFinanceOperationalCapabilityFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_finance_capital_structure_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }
    fetcher = XiaoYuanFinanceCapitalStructureFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_finance_revenue_quality_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }
    fetcher = XiaoYuanFinanceRevenueQualityFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_finance_cash_position_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "period": "annual",
    }
    fetcher = XiaoYuanFinanceCashpositionFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_xy_equity_pledge_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SH600519,SZ002415,AAPL",
        "start_date": date(2021, 1, 1),
        "end_date": date(2023, 1, 10),
    }
    fetcher = XiaoYuanEquityPledgeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# @pytest.mark.record_http
def test_xiaoyuan_per_share_indicator_fetcher(credentials=test_credentials):
    """Test XiaoYuanPerShareIndicatorFetcher."""
    # ["fy", "q1", "q2ytd", "q3ytd", "annual"]
    params = {"symbol": "SH600519", "period": "annual"}

    fetcher = XiaoYuanPerShareIndicatorFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
