from typing import Sequence, Optional
from Utilities.Address import Address
from Aggregates.Item.Item import Item
from Aggregates.Farmer.Farmer import Farmer
from Aggregates.Shopper.Shopper import Shopper


class Order:
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id: str,
        shopperAddress: Shopper[Address],
        farmerAddress: Farmer[Address],
        items: Optional[Sequence[Item]] = []
    ):

        self.id: str = id,
        self.shopperAddress: Address = shopperAddress,
        self.farmerAddress: Address = farmerAddress,
        self.items: Optional[Sequence[Item]] = items

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Order):
            return self.id == o.id

        return False
