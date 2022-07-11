from fastapi import APIRouter
from schema import Ingest


router = APIRouter()


@router.post("/ingest/")
async def ingest_data(timestamp: Ingest.timestamp, base: Ingest.base, date: Ingest.date, rates: Ingest.rates, tags=["ingest_data"]):
    return {"timestamp": timestamp,
            "base": base,
            "date": date,
            "rates": rates
    }
