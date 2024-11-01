"""Equity Router."""

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

from openbb_xiaoyuan.extensions.equity.price.price_router import router as price_router
from openbb_xiaoyuan.extensions.equity.fundamental.fundamental_router import (
    router as fundamental_router,
)

equity_router = Router(prefix="")
equity_router.include_router(fundamental_router)
equity_router.include_router(price_router)


@equity_router.command(
    model="HistoricalMarketCap",
    examples=[
        APIEx(
            parameters={
                "symbol": "SH600519",
                "start_date": "2024-01-01",
                "end_date": "2024-02-10",
                "provider": "xiaoyuan",
            }
        )
    ],
)
async def historical_market_cap(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get the historical market cap of a ticker symbol."""
    return await OBBject.from_query(Query(**locals()))
