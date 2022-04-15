from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Infrastructure.Repositories.Database import get_db
from Infrastructure.Config.token import create_access_token
from Infrastructure.Config.hashing import Hashing

from Domain.Aggregates.Shopper import Shopper
from Domain.Aggregates.Farmer import Farmer


router = APIRouter(tags=["Authentication"])


@router.post("/shopper/login")
def Shopperlogin(
    request: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    shopper = db.query(Shopper).filter(
        Shopper.email == request.username).first()
    if not shopper:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{"Invalid Credentials"}'
        )
    if not Hashing.verify(shopper.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{"Incorrect password"}'
        )

    access_token = create_access_token(data={"sub": shopper.email})

    response = {
        "id": shopper.id,
        "name": shopper.name,
        "email": shopper.email,
        "jwtToken": access_token
    }

    return response


@router.post("/farmer/login")
def Farmerlogin(
    request: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    farmer = db.query(Farmer).filter(
        Farmer.email == request.username).first()
    if not farmer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{"Invalid Credentials"}'
        )
    if not Hashing.verify(farmer.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{"Incorrect password"}'
        )

    access_token = create_access_token(data={"sub": farmer.email})

    response = {
        "id": farmer.id,
        "name": farmer.name,
        "email": farmer.email,
        "jwtToken": access_token
    }

    return response

