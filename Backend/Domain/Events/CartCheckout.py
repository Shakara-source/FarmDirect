from pydantic import BaseModel
from Aggregates.Order.OrderItems import OrderItems
from typing import List


class CartCheckout(BaseModel):

    items: List[OrderItems]
