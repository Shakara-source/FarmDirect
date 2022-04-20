from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Infrastructure.Repositories.Database import get_db
from Infrastructure.Config.token import create_access_token
from Infrastructure.Config.hashing import Hashing
from Infrastructure.Middleware import AuthShopper

from Domain.Aggregates.Shopper import Shopper
from Domain.Aggregates.Farmer import Farmer


router = APIRouter(tags=["Authentication"])


@router.post("/new")
def NewShopper(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    pass


@router.get("/{id}")
def GetShopper(id: int):

    pass


@router.put("/{id}", dependencies=[Depends(AuthShopper)])
def EditShopper(id: int):
    pass


@router.delete("/{id}", dependencies=[Depends(AuthShopper)])
def DeleteOrder(id: int):
    pass
