from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Ingest(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(Integer)
    base = Column(String)
    date = Column(String)
    rates = Column(String)
