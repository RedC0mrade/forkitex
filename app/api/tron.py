from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.tron import (
    TronInfo,
    TronRequestCreate,
    TronRequestOut,
)
from app.services.tron import get_wallet_info
from app.crud.tron import get_requests, create_tron_request
from app.core.factories.database import db_helper

router = APIRouter()


@router.post("/wallet_info", response_model=TronInfo)
async def get_wallet_information(
    request: TronRequestCreate, session: AsyncSession = Depends(db_helper)
):
    await create_tron_request(session=session, request=request)
    return await get_wallet_info(request.wallet_address)


@router.get("/requests", response_model=list[TronRequestOut])
async def read_requests(
    skip: int = 0, limit: int = 10, session: AsyncSession = Depends(db_helper)
):
    return await get_requests(session=session, skip=skip, limit=limit)
