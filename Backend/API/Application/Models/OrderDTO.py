from datetime import date
from py_dto import DTO
from typing import List


class CardSchema(DTO):

    cardNumber: int
    expiration: date
    cvv: str


class OrderItemSchema(DTO):

    itemId: str
    farmerId: str
    price: float
    quantity: int


class CreateOrderSchema(DTO):

    token: str
    payment: CardSchema
    items: List[OrderItemSchema]


class OrderNotificationSchema(DTO):

    farmer_email: str
    items: List[OrderItemSchema]


