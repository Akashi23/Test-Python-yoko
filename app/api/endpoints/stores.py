from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps

router = APIRouter()


@router.post("", response_model=schemas.Store)
def create_store(
    *,
    db: Session = Depends(deps.get_db),
    store_in: schemas.StoreCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new store.
    """
    store = crud.store.create(db=db, obj_in=store_in)
    return store


@router.get("", response_model=List[schemas.Store])
def read_stores(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve stores.
    """
    user_type = current_user.type
    phone_number = current_user.phone_number
    stores = crud.store.get_stores_by_phone_number(db, user_type=user_type, phone_number=phone_number, skip=skip, limit=limit)
    return stores