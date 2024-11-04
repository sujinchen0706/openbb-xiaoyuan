"""xiaoyuan fundamental router. """

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="/fundamental")


@router.command(
    model="EnterpriseLifeCycle",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def enterprise_life_cycle(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="ReductionPercentage",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "start_date": "2021-01-01",
                "end_date": "2023-01-10",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def calculate_reduction_percentage(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="StName",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "start_date": "2021-01-01",
                "end_date": "2023-01-10",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def st_name(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="DuPontAnalysis",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def du_pont_analysis(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinancialDerivative",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def financial_derivative_data(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinancialTTMIndicators",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def financial_ttm_indicators(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="PerShareIndicator",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def per_share_indicator(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinanceProfitAbility",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_profit_ability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinanceGrowthAbility",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_growth_ability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinanceDebtpayingAbility",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_debt_paying_ability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CashFlowStatement",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def cash(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinanceOperationalCapability",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_operational_capability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinanceCapitalStructure",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_capital_structure(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinanceRevenueQuality",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_revenue_quality(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinanceCashposition",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_cash_position(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EquityPledge",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "start_date": "2020-01-01",
                "end_date": "2021-01-01",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def equity_pledge(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="BalanceSheet",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def balance(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="IncomeStatement",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def income(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="KeyMetrics",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def metrics(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FinancialRatios",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def finance_ratios(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CashFlowStatementGrowth",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def cash_growth(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="BalanceSheetGrowth",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def balance_growth(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EquityValuationMultiples",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def multiples(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="IncomeStatementGrowth",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def income_growth(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get the growth of a company's income statement items over time."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="HistoricalDividends",
    examples=[APIEx(parameters={"symbol": "SH600519", "provider": "xiaoyuan"})],
)
async def dividends(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical dividend data for a given company."""
    return await OBBject.from_query(Query(**locals()))
