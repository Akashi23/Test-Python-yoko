from typing import Optional
from datetime import date

from pydantic import BaseModel


# Shared properties
class VisitBase(BaseModel):
    created: Optional[date]
    executor: Optional[int]
    order_id: Optional[int]
    where: Optional[int]

class VisitCreate(VisitBase):
    executor: int
    order_id: str
    where: int


class VisitUpdate(VisitBase):
    pass


class VisitInDBBase(VisitBase):
    id: int
    created: date
    executor: int
    order_id: int
    where: int
    

    class Config:
        orm_mode = True


# Properties to return to Visit
class Visit(VisitInDBBase):
    pass


# Properties properties Visitd in DB
class VisitInDB(VisitInDBBase):
    pass