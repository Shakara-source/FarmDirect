from typing import Sequence, Optional
from Utilities.Address import Address
from Aggregates.Item.Item import Item


class Order:
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id: str,
        shopperAddress: Address,
        farmerAddress: Address,
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
