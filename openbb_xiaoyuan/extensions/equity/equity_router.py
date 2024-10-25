from openbb_core.app.router import Router
from openbb_xiaoyuan.extensions.equity.fundamental.fundamental_router import (
    router as fundamental_router,
)
from openbb_xiaoyuan.extensions.equity.price.price_router import router as price_router

router = Router(prefix="/equity")
router.include_router(fundamental_router)
router.include_router(price_router)
