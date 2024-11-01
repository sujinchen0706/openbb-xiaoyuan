"""openbb_xiaoyuan price router."""

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

router = Router(prefix="/price")


@router.command(
    model="EquityHistorical",
    examples=[
        APIEx(parameters={"symbol": "SH600519", "provider": "xiaoyuan"}),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical price data for a given stock. This includes open, high, low, close, and volume."""
    return await OBBject.from_query(Query(**locals()))
