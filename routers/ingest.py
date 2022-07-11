from fastapi import APIRouter
from schema import Values


router = APIRouter()


@router.post("/ingest/")
async def ingest_data(numbers: Values, tags=["ingest_data"]):
    return {"success": "true"}
