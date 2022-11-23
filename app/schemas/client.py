from typing import Optional

from pydantic import BaseModel


# Shared properties
class ClientBase(BaseModel):
    user_id: Optional[int]


class ClientCreate(ClientBase):
    user_id: int


class ClientUpdate(ClientBase):
    pass


class ClientInDBBase(ClientBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Client(ClientInDBBase):
    pass


# Properties properties stored in DB
class ClientInDB(ClientInDBBase):
    pass