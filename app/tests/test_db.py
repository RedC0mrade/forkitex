import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.crud.tron import create_tron_request
from app.schemas.tron import WalletCreate
from app.core.models.base_model import Base

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL, echo=True)

TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest.mark.asyncio
async def test_create_tron_request():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestingSessionLocal() as session:
        wallet = WalletCreate(
            wallet_address="TKn55gKbKeK6UcWEKPhupkVEFkxu3Q1nkA"
        )
        created = await create_tron_request(
            session=session,
            wallet=wallet,
        )
        assert created.wallet_address == "TKn55gKbKeK6UcWEKPhupkVEFkxu3Q1nkA"
