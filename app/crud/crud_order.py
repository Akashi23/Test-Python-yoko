from typing import List
from datetime import datetime
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

    def validate_user_to_order(self, db: Session, *, order_id: int, user_id: int, user_type: str) -> bool:
        order: Order

        if user_type == 'worker':
            order = (db.query(self.model)
                        .filter(Order.id == order_id, Order.executor == user_id)
                        .first())
        else:
            order = (db.query(self.model)
                        .filter(Order.id == order_id, Order.author == user_id)
                        .first())

        if not order:
            return False
        return True

    def validate_ended_time(self, db: Session, *, order_id: int) -> bool:
        current_datetime = datetime.now()

        order: Order = (db.query(self.model)
                .filter(Order.id == order_id)
                .first())

        if order.ended < current_datetime:
            return False
        return True

    def get_orders(
        self, db: Session, *, user_id: int, user_type: int, skip: int = 0, limit: int = 100
    ) -> List[Order]:
        if user_type == 'worker':
            return (
                db.query(self.model)
                .filter(Order.executor == user_id)
                .offset(skip)
                .limit(limit)
                .all()
            )

        elif user_type == 'client':
            return (
                db.query(self.model)
                .filter(Order.executor == user_id)
                .offset(skip)
                .limit(limit)
                .all()
            )

        return []

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