from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.worker import Worker
from schemas.worker import WorkerCreate, WorkerUpdate


class CRUDWorker(CRUDBase[Worker, WorkerCreate, WorkerUpdate]):
    def create(self, db: Session, *, obj_in: WorkerCreate) -> Worker:
        db_obj = Worker(
            user_id=obj_in.user_id,
            store_id=obj_in.store_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


worker = CRUDWorker(Worker)