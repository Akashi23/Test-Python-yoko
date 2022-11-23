from typing import List
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.order import Order
from schemas.order import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    def create(self, db: Session, *, obj_in: OrderCreate) -> Order:
        db_obj = Order(
            ended=obj_in.ended,
            where=obj_in.where,
            author=obj_in.author,
            status=obj_in.status,
            executor=obj_in.executor
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_order_by_author(
        self, db: Session, *, author: int, skip: int = 0, limit: int = 100
    ) -> List[Order]:
        return (
            db.query(self.model)
            .filter(Order.author == author)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_order_by_executor(
        self, db: Session, *, executor: int, skip: int = 0, limit: int = 100
    ) -> List[Order]:
        return (
            db.query(self.model)
            .filter(Order.executor == executor)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_order_by_store(
        self, db: Session, *, store: int, skip: int = 0, limit: int = 100
    ) -> List[Order]:
        return (
            db.query(self.model)
            .filter(Order.where == store)
            .offset(skip)
            .limit(limit)
            .all()
        )

order = CRUDOrder(Order)