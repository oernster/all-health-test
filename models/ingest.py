from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship

from database import Base


class Ingest(Base):
    __tablename__ = "exchange_rates"

    updated = Column('updated', DATETIME, index=False, nullable=False, primary_key=True)
    timestamp = Column(Integer)
    base = Column(String, index=True)
    date = Column(String)
    rates = Column(String)
