"""openbb_xiaoyuan fundamental router. """

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
    model="XiaoYuanEnterpriseLifeCycle",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanCalculateReductionPercentage",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "start_date": "2021-01-01",
                "end_date": "2023-01-10",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanStName",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "start_date": "2021-01-01",
                "end_date": "2023-01-10",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanDuPontAnalysis",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinancialDerivative",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinancialTTMIndicators",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanPerShareIndicatorFetcher",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinanceProfitAbility",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinanceGrowthAbility",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinanceDebtpayingAbility",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanCashFlowStatement",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinanceOperationalCapability",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinanceCapitalStructure",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinanceRevenueQuality",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanFinanceCashposition",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "period": "annual",
                "provider": "openbb_xiaoyuan",
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
    model="XiaoYuanEquityPledge",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "start_date": "2020-01-01",
                "end_date": "2021-01-01",
                "provider": "openbb_xiaoyuan",
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
