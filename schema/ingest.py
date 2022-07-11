from pydantic import BaseModel
from typing import Dict


class Ingest(BaseModel):
    timestamp: int
    base: str
    date: str
    rates: str
    
    class Config:
        orm_mode = True