"""Calendar Router."""

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

router = Router(prefix="/calendar")

# pylint: disable=unused-argument


@router.command(
    model="CalendarDividend",
    examples=[
        APIEx(parameters={"provider": "xiaoyuan"}),
        APIEx(
            description="Get dividend calendar for specific dates.",
            parameters={
                "start_date": "2024-02-01",
                "end_date": "2024-02-07",
                "provider": "xiaoyuan",
            },
        ),
    ],
)
async def dividend(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming dividend payments. Includes dividend amount, ex-dividend and payment dates."""
    return await OBBject.from_query(Query(**locals()))
