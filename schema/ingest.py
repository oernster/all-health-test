from pydantic import BaseModel


class Ingest(BaseModel):
    country1: str
    