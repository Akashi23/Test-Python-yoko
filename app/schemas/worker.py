from typing import Optional

from pydantic import BaseModel


# Shared properties
class WorkerBase(BaseModel):
    user_id: Optional[int]
    store_id: Optional[int]


class WorkerCreate(WorkerBase):
    user_id: int
    store_id: int


class WorkerUpdate(WorkerBase):
    pass


class WorkerInDBBase(WorkerBase):
    id: int
    user_id: str
    store_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Worker(WorkerInDBBase):
    pass


# Properties properties stored in DB
class WorkerInDB(WorkerInDBBase):
    pass