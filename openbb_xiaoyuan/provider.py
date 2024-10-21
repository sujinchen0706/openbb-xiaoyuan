"""openbb_xiaoyuan OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider

from openbb_xiaoyuan.models.calculate_reduction_percentage import XYCalculateReductionPercentageFetcher
from openbb_xiaoyuan.models.du_pont_analysis import XYDuPontAnalysisFetcher
from openbb_xiaoyuan.models.enterprise_life_cycle import XYEnterpriseLifeCycleFetcher
from openbb_xiaoyuan.models.example import ExampleFetcher
from openbb_xiaoyuan.models.financial_derivative_data import XYFinancialDerivativeFetcher
from openbb_xiaoyuan.models.financial_ttm_indicators import XYFinancialTTMIndicatorsFetcher
from openbb_xiaoyuan.models.st_name import XYStNameFetcher
from openbb_xiaoyuan.models.financial_metrics_per_share import (
    XiaoYuanPerShareIndicatorFetcher,
)
# mypy: disable-error-code="list-item"

provider = Provider(
    name="openbb_xiaoyuan",
    description="Data provider for openbb-xiaoyuan.",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    # credentials=["api_key"],
    website="https://openbb-xiaoyuan.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Example": ExampleFetcher,
        "XYEnterpriseLifeCycle": XYEnterpriseLifeCycleFetcher,
        "XYCalculateReductionPercentage": XYCalculateReductionPercentageFetcher,
        "XYStName": XYStNameFetcher,
        "XYDuPontAnalysis": XYDuPontAnalysisFetcher,
        "XYFinancialDerivative": XYFinancialDerivativeFetcher,
        "XYFinancialTTMIndicators": XYFinancialTTMIndicatorsFetcher,
        "XiaoYuanPerShareIndicatorFetcher": XiaoYuanPerShareIndicatorFetcher,
    },
)
