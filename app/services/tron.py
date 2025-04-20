import json
from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from starlette.concurrency import run_in_threadpool


async def get_wallet_info(address: str) -> dict:
    def fetch():
        client = Tron()
        try:
            balance = client.get_account_balance(address)
            net = client.get_account_resource(address)
            print(json.dumps(net, indent=2))
            return {
                "balance": balance,
                "bandwidth": net.get("freeNetLimit", 0)
                - net.get("freeNetUsed", 0),
                "energy": net.get("EnergyLimit", 0),
            }
        except AddressNotFound:
            return {"balance": 0.0, "bandwidth": 0, "energy": 0}

    return await run_in_threadpool(fetch)
