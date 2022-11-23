from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps

router = APIRouter()


@router.post("", response_model=schemas.Visit)
def create_visit(
    *,
    db: Session = Depends(deps.get_db),
    visit_in: schemas.VisitCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new visit.
    """

    if current_user.type != 'client':
        raise HTTPException(
            status_code=400,
            detail="You are not client, please enter with client account.",
        )

    client = crud.client.get_client_by_user_id(db, user_id=current_user.id)
    
    if not crud.client.validate_client_to_store(db, store_id=visit_in.where, client_id=client.id):
        raise HTTPException(
            status_code=400,
            detail="The client does not exist in the store.",
        )

    if not crud.order.validate_ended_time(db, order_id=visit_in.order_id):
        raise HTTPException(
            status_code=400,
            detail="Order term has ended.",
        )

    if not crud.order.validate_user_to_order(db, order_id=visit_in.order_id, user_id=visit_in.executor, user_type='worker'):
        raise HTTPException(
            status_code=400,
            detail="The worker does not exist in the order.",
        )

    if crud.visit.validate_order_to_visit(db, order_id=visit_in.order_id):
        raise HTTPException(
            status_code=400,
            detail="The order exist in the order.",
        )

    visit = crud.visit.create(db=db, obj_in=visit_in)
    return visit


@router.get("", response_model=List[schemas.Visit])
def read_visits(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve visits.
    """
    visits = crud.visit.get_visits(db, skip=skip, limit=limit)
    return visits
