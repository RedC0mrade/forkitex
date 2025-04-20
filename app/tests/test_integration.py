import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, AsyncMock

from app.main import main_app  # или актуальный путь к FastAPI-приложению


@pytest.mark.asyncio
async def test_wallet_info_and_get_requests():
    mocked_wallet_info = {
        "balance": 123.45,
        "bandwidth": 1000,
        "energy": 500,
    }

    with patch(
        "app.services.tron.get_wallet_info",
        new=AsyncMock(return_value=mocked_wallet_info),
    ):
        transport = ASGITransport(app=main_app)
        async with AsyncClient(
            transport=transport, base_url="http://test"
        ) as ac:
            response = await ac.get("/wallet/info/TTestAddress123")

        assert response.status_code == 200
        assert response.json() == {
            "balance": 123.45,
            "bandwidth": 1000,
            "energy": 500,
            "address": "TTestAddress123",
        }
