from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.store import Store
from schemas.store import StoreCreate, StoreUpdate


class CRUDStore(CRUDBase[Store, StoreCreate, StoreUpdate]):
    def create(self, db: Session, *, obj_in: StoreCreate) -> Store:
        db_obj = Store(
            name=obj_in.name,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

store = CRUDStore(Store)