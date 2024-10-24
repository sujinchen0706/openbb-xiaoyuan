from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="/equity/fundamental")


@router.command(model="XiaoYuanEnterpriseLifeCycle")
async def enterprise_life_cycle(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanCalculateReductionPercentage")
async def calculate_reduction_percentage(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanStName")
async def st_name(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanDuPontAnalysis")
async def du_pont_analysis(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanFinancialDerivative")
async def financial_derivative_data(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanFinancialTTMIndicators")
async def financial_ttm_indicators(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanPerShareIndicatorFetcher")
async def per_share_indicator(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanFinanceProfitAbility")
async def finance_profit_ability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanFinanceGrowthAbility")
async def finance_growth_ability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanFinanceDebtpayingAbility")
async def finance_debt_paying_ability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanCashFlowStatement")
async def cash_flow(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanFinanceOperationalCapability")
async def finance_operational_capability(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(model="XiaoYuanFinanceCapitalStructure")
async def finance_capital_structure(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))
