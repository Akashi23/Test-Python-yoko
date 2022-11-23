from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base_class import Base

class Visit(Base):
    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, nullable=False, server_default=func.now())
    executor = Column(Integer, ForeignKey("worker.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("order.id"))
    order = relationship("Order", back_populates="visit")
    where = Column(Integer, ForeignKey("store.id"), nullable=False)