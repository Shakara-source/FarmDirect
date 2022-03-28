from OrderStatus import OrderStatus
from pydantic import BaseModel


class Order(BaseModel):
    
    """Order represents order type users as an entity"""

    def __init__(
        self,
        status: OrderStatus,
        shopper_id: int,
        total: float,
    ):

        self.id: str = id,
        self.status: OrderStatus = status,
        self.shopper_id: int = shopper_id,
        self.total: float = total

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Order):
            return self.id == o.id

        return False
