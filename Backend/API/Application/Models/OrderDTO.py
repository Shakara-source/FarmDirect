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


class NewOrderSchema(DTO):

    token: str
    payment: CardSchema
    shopperAddress: str
    items: List[OrderItemSchema]


class OrderInvoiceSchema(DTO):

    template: str
    shopperEmail: str
    shopperName: str
    items: List[OrderItemSchema]
    price: float


class FarmerOrderNotificationSchema(DTO):

    template: str
    farmerEmail: str
    farmerName: str
    orderAddress: str
    items: List[OrderItemSchema]
