from fastapi import APIRouter, Depends
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from config.container import Container, inject
# from modules.iam.module import IdentityAndAccessModule
# from modules.iam.application.exceptions import (
#     UserNotFoundException,
#     UsernamePasswordMismatchException,
# )
# from modules.iam.domain.entities import User
# from api.shared import dependency

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

def getFarmerByToken(
    token,
    module: IdentityAndAccessModule = dependency(Container.iam_module),
) -> User:
    user = module.authentication_service.find_user_by_access_token(token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = get_user_by_token(token)
    return user

@router.get('/')


