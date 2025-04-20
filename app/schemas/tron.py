from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TronRequestCreate(BaseModel):
    wallet_address: str


class TronInfo(BaseModel):
    balance: float
    bandwidth: int
    energy: int


class TronRequestOut(BaseModel):
    id: int
    wallet_address: str
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
