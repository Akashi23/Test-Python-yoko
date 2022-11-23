from typing import Optional

from pydantic import BaseModel


# Shared properties
class StoreBase(BaseModel):
    name: Optional[str]


class StoreCreate(StoreBase):
    name: str


class StoreUpdate(StoreBase):
    pass


class StoreInDBBase(StoreBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to Store
class Store(StoreInDBBase):
    pass


# Properties properties stored in DB
class StoreInDB(StoreInDBBase):
    pass