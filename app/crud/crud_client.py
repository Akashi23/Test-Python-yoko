from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.client import Client
from schemas.client import ClientCreate, ClientUpdate


class CRUDClient(CRUDBase[Client, ClientCreate, ClientUpdate]):
    def create(self, db: Session, *, obj_in: ClientCreate) -> Client:
        db_obj = Client(
            user_id=obj_in.user_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

client = CRUDClient(Client)