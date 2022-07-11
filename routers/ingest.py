from fastapi import APIRouter
from schema import Ingest


router = APIRouter()


@router.post("/ingest/")
async def ingest_data(strings: Ingest, tags=["ingest_data"]):
    return {"success": "true"}
