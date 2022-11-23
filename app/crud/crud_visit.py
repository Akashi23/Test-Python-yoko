from typing import List
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.visit import Visit
from schemas.visit import VisitCreate, VisitUpdate


class CRUDVisit(CRUDBase[Visit, VisitCreate, VisitUpdate]):
    def create(self, db: Session, *, obj_in: VisitCreate) -> Visit:
        db_obj = Visit(
            order_id=obj_in.order_id,
            where=obj_in.where,
            executor=obj_in.executor
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_visit_by_executor(
        self, db: Session, *, executor: int, skip: int = 0, limit: int = 100
    ) -> List[Visit]:
        return (
            db.query(self.model)
            .filter(Visit.executor == executor)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_visit_by_order_id(
        self, db: Session, *, order_id: int, skip: int = 0, limit: int = 100
    ) -> List[Visit]:
        return (
            db.query(self.model)
            .filter(Visit.order_id == order_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

visit = CRUDVisit(Visit)