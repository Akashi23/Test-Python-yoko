from typing import List
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.store import Store
from schemas.store import StoreCreate, StoreUpdate
from sqlalchemy.sql import text

class CRUDStore(CRUDBase[Store, StoreCreate, StoreUpdate]):
    def get_stores_by_phone_number(
        self, db: Session, *, user_type: str, phone_number: int, skip: int = 0, limit: int = 100
    ) -> List[Store]:
        statement = text(
        f"""
            SELECT *
                FROM   store
                WHERE  id = (SELECT store_id
                            FROM   {user_type}
                            WHERE  user_id = (SELECT id
                                            FROM   "user"
                                            WHERE  phone_number = '{phone_number}')); 
        """)

        stores_from_db = db.execute(statement)
        stores = [{"id": store[0], "name": store[1]} for store in stores_from_db]

        return stores

    def create(self, db: Session, *, obj_in: StoreCreate) -> Store:
        db_obj = Store(
            name=obj_in.name,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

store = CRUDStore(Store)