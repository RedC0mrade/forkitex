from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.schemas.tron import (
    WalletInfo,
    WalletCreate,
    WalletOut,
)
from app.services.tron import get_wallet_info
from app.crud.tron import get_requests, create_tron_request
from app.core.factories.database import db_helper

router = APIRouter(prefix=settings.api.tron, tags=["tron"])


@router.post("/wallet_info", response_model=WalletInfo)
async def get_wallet_information(
    wallet: WalletCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    await create_tron_request(session=session, wallet=wallet)
    return await get_wallet_info(wallet.wallet_address)


@router.get("/requests", response_model=list[WalletOut])
async def read_requests(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await get_requests(session=session, skip=skip, limit=limit)
