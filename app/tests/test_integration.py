from fastapi.testclient import TestClient
from app.main import main_app

client = TestClient(main_app)


def test_wallet_info_and_get_requests():
    response = client.post(
        "/wallet_info", json={"wallet_address": "TXYZ...1234"}
    )
    assert response.status_code == 200
    assert "balance" in response.json()

    response = client.get("/requests")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
