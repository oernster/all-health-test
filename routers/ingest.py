from fastapi import APIRouter
from schema import Ingest
import crud


router = APIRouter()


@router.post("/ingest/")
async def ingest_data(ingest: Ingest, tags=["ingest_data"]):
    crud.create_ingest(ingest=ingest)
    
    return {ingest}
