from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from starlette.concurrency import run_in_threadpool


async def get_wallet_info(address: str) -> dict:
    async def fetch():
        client = Tron()
        try:
            balance = client.get_account_balance(address)
            net = client.get_account_resource(address)
            return {
                "balance": balance,
                "bandwidth": net.get("free_net_limit", 0),
                "energy": net.get("EnergyLimit", 0),
            }
        except AddressNotFound:
            return {"balance": 0.0, "bandwidth": 0, "energy": 0}

    return await run_in_threadpool(fetch)
