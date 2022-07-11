from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import Ingest
from database import get_db
import crud


router = APIRouter()

@router.get("/exchange_rates/{currency}/{date}")
async def get_exchange_rates(currency, date, db: Session = Depends(get_db)):    
    return crud.get_exchange_rates(currency=currency, date=date, db=db)
