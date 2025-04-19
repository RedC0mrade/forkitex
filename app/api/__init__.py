from fastapi import APIRouter
from app.core.config import settings
from .tron import router as router_tron

router = APIRouter(prefix=settings.api.prefix)

router.include_router(router_tron)
