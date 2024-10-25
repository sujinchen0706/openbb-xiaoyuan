from openbb_core.app.router import Router

from openbb_xiaoyuan.extensions.equity.equity_router import router as equity_router

router = Router(prefix="")
router.include_router(equity_router)
