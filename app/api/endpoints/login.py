from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import models, schemas
from schemas.user import UserLogin
from api import deps
from core import security
from core.config import settings
from crud import crud_user

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db),user_in: UserLogin = Body(None)
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    if not user_in:
        raise HTTPException(status_code=400, detail="Empty body")
    user = crud_user.user.authenticate(
        db, email=user_in.email, password=user_in.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud_user.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user
