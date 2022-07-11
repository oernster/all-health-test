from pydantic import BaseModel


class Ingest(BaseModel):
    timestamp: int
    base: str
    date: str
    rates: str
    
    class Config:
        orm_mode = True