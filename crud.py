from sqlalchemy.orm import Session
from fastapi import Depends
from .database import get_db

from .models.ingest import Ingest as Ingest_model
from .schema.ingest import Ingest as Ingest_schema


def create_ingest(ingest: Ingest_schema, db: Session = Depends(get_db)):
    db_ingest = Ingest_model(**ingest.dict())
    db.add(db_ingest)
    db.commit()
    db.refresh(db_ingest)
    return db_ingest
