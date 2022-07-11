from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import Depends
from database import get_db

from models.ingest import Ingest as Ingest_model
from schema.ingest import Ingest as Ingest_schema


def create_ingest(db: Session, ingest: Ingest_schema):
    db_ingest = Ingest_model(updated=datetime.now(),
                             timestamp=ingest.timestamp,
                             base=ingest.base,
                             date=ingest.date,
                             rates=ingest.rates)
    db.add(db_ingest)
    db.commit()
    db.refresh(db_ingest)
    return db_ingest

def get_exchange_rates(db: Session, currency):
    return db.query(Ingest_model).filter(Ingest_model.base == currency).order_by(desc('updated')).first()

