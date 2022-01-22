from typing import Sequence, Optional
from Aggregates.Item.Item import Item
from Aggregates.Shopper.Shopper import Shopper


class Cart:
    """Cart represents shopping cart type users as an entity"""

    def __init__(
        self,
        id: str,
        shopperId: Shopper['id'],
        shopper: Shopper,
        items: Optional[Sequence[Item]] = []
    ):

        self.id: str = id,
        self.shopper: Shopper = shopper,
        self.shopperId: str = shopperId,
        self.items: Optional[Sequence[Item]] = items
        
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Cart):
            return self.id == o.id

        return False
