from fastapi import APIRouter
from schema import Ingest
import crud


router = APIRouter()


@router.post("/ingest/")
async def ingest_data(timestamp: Ingest.timestamp, base: Ingest.base, date: Ingest.date, rates: Ingest.rates, tags=["ingest_data"]):
    crud.create_ingest(timestamp=timestamp, base=base, date=date, rates=rates)
    
    return {"timestamp": timestamp,
            "base": base,
            "date": date,
            "rates": rates
    }
