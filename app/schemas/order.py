from typing import Optional
from datetime import date

from pydantic import BaseModel


# Shared properties
class OrderBase(BaseModel):
    created: Optional[date]
    ended: Optional[date]
    where: Optional[int]
    author: Optional[int]
    status: Optional[str]
    executor: Optional[int]

class OrderCreate(OrderBase):
    ended: date
    where: int
    author: int
    status: str
    executor: int


class OrderUpdate(OrderBase):
    pass


class OrderInDBBase(OrderBase):
    id: int
    created: date
    ended: date
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