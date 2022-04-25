from pydantic.dataclasses import dataclass


@dataclass
class OrderItems:

    orderId: str
    itemId: str
    farmerId: str
    price: float
    quantity: int
