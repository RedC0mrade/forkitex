from app.core.config import settings
from .tron import router

router.include_router(
    router,
    prefix=settings.api,
)
