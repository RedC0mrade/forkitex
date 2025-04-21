from pydantic import BaseModel, ConfigDict
from datetime import datetime


class WalletCreate(BaseModel):
    wallet_address: str


class WalletInfo(BaseModel):
    balance: float
    bandwidth: int
    energy: int


class WalletOut(BaseModel):
    id: int
    wallet_address: str
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
