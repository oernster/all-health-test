from typing import Optional
from fastapi import FastAPI
from routers import main, ingest


app = FastAPI()


app.include_router(main.router)
app.include_router(ingest.router)
