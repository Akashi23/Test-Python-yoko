from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base_class import Base

class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, nullable=False, server_default=func.now())
    ended = Column(DateTime, nullable=False)
    where = Column(Integer, ForeignKey("store.id"), nullable=False)
    author = Column(Integer, ForeignKey("client.id"), nullable=False)
    # status = Column(Integer, ForeignKey("store.id"))
    executor = Column(Integer, ForeignKey("worker.id"), nullable=False)