from pydantic import BaseModel
from typing import List
from Domain.Aggregates.Order import Order, OrderStatus, OrderItems


class OrderReadModel(BaseModel):

    """OrderReadModel represents data structure as a read model."""

    id: str = '',
    status: OrderStatus = '',
    shopper_id: str = '',
    items: List[OrderItems] = [],
    total: float = 0.0

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(Order: Order) -> "OrderReadModel":
        return OrderReadModel(
            id=Order.id,
            status=Order.status,
            shopper_id=Order.shopper_id,
            items=Order.items,
            total=Order.total
        )
