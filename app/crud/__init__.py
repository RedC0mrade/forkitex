from sqlalchemy.orm import Session
from . import models, schemas


def create_tron_request(db: Session, request: schemas.TronRequestCreate):
    db_request = models.TronRequest(wallet_address=request.wallet_address)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def get_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TronRequest).offset(skip).limit(limit).all()
