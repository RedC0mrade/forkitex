from fastapi import APIRouter
from .tron import router as router_tron

router = APIRouter()

router.include_router(router_tron)
