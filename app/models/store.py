from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

class Store(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    workers = relationship("Worker", back_populates="store")