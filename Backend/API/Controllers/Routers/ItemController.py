from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Infrastructure.Repositories.Database import get_db
from Infrastructure.Config.token import create_access_token
from Infrastructure.Config.hashing import Hashing
from Infrastructure.Middleware import AuthFarmer
from Application.Queries.ItemQueries import ItemQuerySwitchboard

from Domain.Aggregates.Shopper import Shopper
from Domain.Aggregates.Farmer import Farmer


router = APIRouter(tags=["Authentication"])


@router.post("/new", dependencies=[Depends(AuthFarmer)])
def NewItem(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    pass


@router.get("/by/{function}")
def ItemBy(function: str, request: ItemDTO):

    info = request.data
    return ItemQuerySwitchboard(function, info)


@router.put("/{id}", dependencies=[Depends(AuthFarmer)])
def EditItem(id: int):
    pass


@router.delete("/{id}", dependencies=[Depends(AuthFarmer)])
def DeleteItem(id: int):
    pass
