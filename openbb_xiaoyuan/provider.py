"""openbb_xiaoyuan OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider

from openbb_xiaoyuan.models.balance_sheet import XiaoYuanBalanceSheetFetcher
from openbb_xiaoyuan.models.balance_sheet_growth import (
    XiaoYuanBalanceSheetGrowthFetcher,
)
from openbb_xiaoyuan.models.cash_flow import XiaoYuanCashFlowStatementFetcher
from openbb_xiaoyuan.models.cash_flow_growth import (
    XiaoYuanCashFlowStatementGrowthFetcher,
)
from openbb_xiaoyuan.models.equity_historical import XiaoYuanEquityHistoricalFetcher
from openbb_xiaoyuan.models.financial_ratios import XiaoYuanFinancialRatiosFetcher
from openbb_xiaoyuan.models.income_statement import XiaoYuanIncomeStatementFetcher

# from openbb_xiaoyuan.models.key_metrics import XiaoYuanKeyMetricsFetcher

from openbb_xiaoyuan.models.income_statement_growth import (
    XiaoYuanIncomeStatementGrowthFetcher,
)

# mypy: disable-error-code="list-item"


openbb_xiaoyuan_provider = Provider(
    name="xiaoyuan",
    description="Data provider for openbb-xiaoyuan.",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    # credentials=["api_key"],
    website="https://openbb-xiaoyuan.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "CashFlowStatement": XiaoYuanCashFlowStatementFetcher,
        "FinancialRatios": XiaoYuanFinancialRatiosFetcher,
        "CashFlowStatementGrowth": XiaoYuanCashFlowStatementGrowthFetcher,
        "BalanceSheetGrowth": XiaoYuanBalanceSheetGrowthFetcher,
        "BalanceSheet": XiaoYuanBalanceSheetFetcher,
        "IncomeStatement": XiaoYuanIncomeStatementFetcher,
        "IncomeStatementGrowth": XiaoYuanIncomeStatementGrowthFetcher,
        "EquityHistorical": XiaoYuanEquityHistoricalFetcher,
        # "KeyMetrics": XiaoYuanKeyMetricsFetcher,
    },
)
