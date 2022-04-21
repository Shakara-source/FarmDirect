from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Infrastructure.Repositories.Database import get_db
from Infrastructure.Config.token import create_access_token
from Infrastructure.Config.hashing import Hashing
from Infrastructure.Middleware import AuthFarmer
from Application.Queries.FarmerQueries import FarmerQueries

from Domain.Aggregates.Shopper import Shopper
from Domain.Aggregates.Farmer import Farmer


router = APIRouter(tags=["Authentication"])


@router.post("/new")
def NewFarmer(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    pass


@router.get("/{id}")
def GetFarmer(id: int, db: Session = Depends(get_db)):

    return FarmerQueries.findById(id=id, db=db)


@router.put("/{id}", dependencies=[Depends(AuthFarmer)])
def EditFarmer(id: int):
    pass


@router.delete("/{id}", dependencies=[Depends(AuthFarmer)])
def DeleteFarmer(id: int):
    pass
