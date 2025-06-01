from datetime import timedelta
from typing import Any
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter
from pydantic.schema import schema
from sqlalchemy.orm.session import Session
from app.schemas.user import UserToken

from app.api import deps
from app.core.config import settings
from app.api.deps import get_current_user
from app import crud
from app.core.auth import create_access_token
from app.schemas.auth import LoginResponse

router = APIRouter(prefix=settings.AUTH_PREFIX, tags=["Auth"])


@router.post(settings.TOKEN_ENDPOINT,
             summary="authenticate the user",
             response_model=LoginResponse)
def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = crud.user.get_by_email(db=db, email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    if not crud.user.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    active_user = dict(UserToken.from_orm(user))
    return LoginResponse(access_token=create_access_token(active_user, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)), token_type="bearer")
