from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

class Visit(Base):
    id = Column(Integer, primary_key=True, index=True)

    