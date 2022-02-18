from typing import Sequence, Optional
import OrderStatus
from Aggregates.Item.Item import Item
from Aggregates.Farmer import Farmer
from Aggregates.Shopper import Shopper


class Order:
    
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id: str,
        status: OrderStatus,
        shopper: Shopper,
        farmer: Farmer,
        items: Optional[Sequence[Item]] = []
    ):

        self.id: str = id,
        self.status: OrderStatus = status,
        self.shopper: Shopper = shopper,
        self.farmer: Farmer = farmer,
        self.items: Optional[Sequence[Item]] = items

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Order):
            return self.id == o.id

        return False
