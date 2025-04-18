from sqlalchemy import DateTime, String, func
from datetime import datetime
from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column


class TronRequest(Base):
    __tablename__ = "tron_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    wallet_address: Mapped[str] = mapped_column(
        String,
        index=True,
    )
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
