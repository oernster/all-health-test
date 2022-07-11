from typing import Optional
from fastapi import FastAPI
from routers import main, ingest
from database import SessionLocal, engine, Base
import models


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(main.router)
app.include_router(ingest.router)
