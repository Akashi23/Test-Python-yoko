from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

class Worker(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="worker_id")
    store_id = Column(Integer, ForeignKey("store.id"))
    store = relationship("Store", back_populates="workers")
    orders = relationship("Order")