from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.client import Client
from schemas.client import ClientCreate, ClientUpdate


class CRUDClient(CRUDBase[Client, ClientCreate, ClientUpdate]):
    def create(self, db: Session, *, obj_in: ClientCreate) -> Client:
        db_obj = Client(
            user_id=obj_in.user_id,
            store_id=obj_in.store_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_client_by_user_id(self, db: Session, *, user_id: int) -> Client:
        return (
            db.query(self.model)
            .filter(Client.user_id == user_id)
            .first()
        )


    def validate_client_to_store(self, db: Session, *, store_id: int, client_id: int) -> bool:
        client = (db.query(self.model)
                    .filter(Client.id == client_id, Client.store_id == store_id)
                    .first())
                    
        if not client:
            return False
        return True

client = CRUDClient(Client)