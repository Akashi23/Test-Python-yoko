from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel


# Shared properties
class OrderBase(BaseModel):
    created: Optional[datetime]
    ended: Optional[datetime]
    where: Optional[int]
    author: Optional[int]
    status: Optional[str]
    executor: Optional[int]

class OrderCreate(OrderBase):
    ended: datetime
    where: int
    author: int
    status: str
    executor: int


class OrderUpdate(OrderBase):
    pass


class OrderInDBBase(OrderBase):
    id: int
    created: datetime
    ended: datetime
    where: int
    author: int
    status: str
    executor: int

    class Config:
        orm_mode = True


# Properties to return to Order
class Order(OrderInDBBase):
    pass


# Properties properties Orderd in DB
class OrderInDB(OrderInDBBase):
    pass