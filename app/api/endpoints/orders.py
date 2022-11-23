from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps

router = APIRouter()


@router.post("", response_model=schemas.Order)
def create_order(
    *,
    db: Session = Depends(deps.get_db),
    order_in: schemas.OrderCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new order.
    """

    if current_user.type != 'client':
        raise HTTPException(
            status_code=400,
            detail="You are not client, please enter with client account.",
        )

    order_in.status = 'started'

    if not crud.worker.validate_worker_to_store(db, store_id=order_in.where, worker_id=order_in.executor):
        raise HTTPException(
            status_code=400,
            detail="The worker does not exist in the store.",
        )

    if not crud.client.validate_client_to_store(db, store_id=order_in.where, client_id=order_in.author):
        raise HTTPException(
            status_code=400,
            detail="The client does not exist in the store.",
        )

    order = crud.order.create(db=db, obj_in=order_in)
    return order


@router.get("", response_model=List[schemas.Order])
def read_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve orders.
    """
    user_type = current_user.type
    user_id = current_user.id
    orders = crud.order.get_orders(db, user_id=user_id, user_type=user_type, skip=skip, limit=limit)
    return orders


@router.put("/{order_id}", response_model=schemas.Order)
def update_order(
    *,
    db: Session = Depends(deps.get_db),
    order_id: int,
    order_in: schemas.OrderCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update order.
    """
    if order_in.status not in ['ended', 'in process', 'awaiting', 'canceled']:
        raise HTTPException(
            status_code=400,
            detail="Incorrect status. Choose between 'ended', 'in process', 'awaiting', 'canceled'.",
        )

    order = crud.order.update(db=db, obj_in=order_in)
    return order