from sqlalchemy.orm import Session

import schemas
from crud.crud_user import user
from core.config import settings
from db.base_class import Base
from db.session import engine

def init_db(db: Session) -> None:

    Base.metadata.create_all(bind=engine)

    user_obj = user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user_obj:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            phone_number='87771112233',
            type='superadmin',
        )
        user_obj = user.create(db, obj_in=user_in) 