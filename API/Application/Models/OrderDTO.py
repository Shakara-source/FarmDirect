from datetime import datetime
from py_dto import DTO
from typing import List


class CardSchema(DTO):

    cardNumber: int
    expiration: datetime
    cvv: int


class TokenSchema(DTO):

    id: str
    email: str
    card: CardSchema


class ItemSchema(DTO):

    name: str
    description: str
    price: float
    category: str
    status: str
    quantity: int


class CreateOrderSchema(DTO):

    token: TokenSchema
    items: List[ItemSchema]
    subtotal: int
