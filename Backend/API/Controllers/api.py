from fastapi import FastAPI
from Infrastructure.Repositories import engine, Base
from routers import (
    AuthController,
    FarmerController,
    ItemController,
    ShopperController,
    OrderController
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(HTTPSRedirectMiddleware)

Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return "Hello"


app.include_router(AuthController.router)
app.include_router(FarmerController.router)
app.include_router(ShopperController.router)
app.include_router(ItemController.router)
app.include_router(OrderController.router)
