from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.models.tron import TronRequest
from app.schemas.tron import WalletCreate


async def create_tron_request(session: AsyncSession, wallet: WalletCreate):
    db_request = TronRequest(wallet_address=wallet.wallet_address)
    session.add(db_request)
    await session.commit()
    await session.refresh(db_request)
    return db_request


async def get_requests(session: AsyncSession, skip: int = 0, limit: int = 10):
    result = await session.execute(
        select(TronRequest).offset(skip).limit(limit)
    )
    return result.scalars().all()
