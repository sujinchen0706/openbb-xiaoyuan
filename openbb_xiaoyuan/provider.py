"""openbb_xiaoyuan OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider

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
from openbb_xiaoyuan.models.finance_debt_paying_ability import (
    XiaoYuanFinanceDebtpayingAbilityFetcher,
)
from openbb_xiaoyuan.models.finance_growth_ability import (
    XiaoYuanFinanceGrowthAbilityFetcher,
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
from openbb_xiaoyuan.models.financial_ttm_indicators import (
    XiaoYuanFinancialTTMIndicatorsFetcher,
)
from openbb_xiaoyuan.models.st_name import XiaoYuanStNameFetcher
from openbb_xiaoyuan.models.financial_metrics_per_share import (
    XiaoYuanPerShareIndicatorFetcher,
)
from openbb_xiaoyuan.models.financial_ratios import (
    XiaoYuanFinancialRatiosFetcher,
)
from openbb_xiaoyuan.models.cash_flow_growth import (
    XiaoYuanCashFlowStatementGrowthFetcher,
)
from openbb_xiaoyuan.models.balance_sheet_growth import (
    XiaoYuanBalanceSheetGrowthFetcher,
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
        "EnterpriseLifeCycle": XiaoYuanEnterpriseLifeCycleFetcher,
        "CalculateReductionPercentage": XiaoYuanCalculateReductionPercentageFetcher,
        "StName": XiaoYuanStNameFetcher,
        "DuPontAnalysis": XiaoYuanDuPontAnalysisFetcher,
        "FinancialDerivative": XiaoYuanFinancialDerivativeFetcher,
        "FinancialTTMIndicators": XiaoYuanFinancialTTMIndicatorsFetcher,
        "PerShareIndicatorFetcher": XiaoYuanPerShareIndicatorFetcher,
        "FinanceProfitAbility": XiaoYuanFinanceProfitAbilityFetcher,
        "FinanceDebtpayingAbility": XiaoYuanFinanceDebtpayingAbilityFetcher,
        "FinanceGrowthAbility": XiaoYuanFinanceGrowthAbilityFetcher,
        "CashFlowStatement": XiaoYuanCashFlowStatementFetcher,
        "FinanceOperationalCapability": XiaoYuanFinanceOperationalCapabilityFetcher,
        "FinanceCapitalStructure": XiaoYuanFinanceCapitalStructureFetcher,
        "FinanceRevenueQuality": XiaoYuanFinanceRevenueQualityFetcher,
        "FinanceCashposition": XiaoYuanFinanceCashpositionFetcher,
        "EquityPledge": XiaoYuanEquityPledgeFetcher,
        "FinancialRatios": XiaoYuanFinancialRatiosFetcher,
        "CashFlowStatementGrowth": XiaoYuanCashFlowStatementGrowthFetcher,
        "BalanceSheetGrowth": XiaoYuanBalanceSheetGrowthFetcher,
    },
)
