from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema import Ingest
from database import get_db
import crud


router = APIRouter()

@router.post("/ingest")
async def ingest_data(ingest: Ingest, db: Session = Depends(get_db)):
    return crud.create_ingest(ingest=ingest, db=db)
