from fastapi.testclient import TestClient
from app.main import main_app
import pytest

client = TestClient(main_app)


@pytest.mark.asyncio
async def test_get_wallet_information():
    request_data = {"wallet_address": "TDQT4KKSEdJwAaGvkXFHkX61Fo1soLCxo4"}

    response = client.post("/forkytech/tron/wallet_info", json=request_data)

    assert response.status_code == 200

    response_data = response.json()
    assert "balance" in response_data
    assert "bandwidth" in response_data
    assert "energy" in response_data
    assert isinstance(response_data["balance"], float)
    assert isinstance(response_data["bandwidth"], int)
    assert isinstance(response_data["energy"], int)
