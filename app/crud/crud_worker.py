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

    def validate_worker_to_store(self, db: Session, *, store_id: int, worker_id: int) -> bool:
        worker = (db.query(self.model)
                    .filter(Worker.id == worker_id, Worker.store_id == store_id)
                    .first())
                    
        if not worker:
            return False
        return True


worker = CRUDWorker(Worker)