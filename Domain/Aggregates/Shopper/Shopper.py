from typing import Sequence, Optional
from Utilities.Address import Address
from Aggregates.Order.Order import Order
from Aggregates.Farmer.Farmer import Farmer


class Shopper:
    """Farmer represents farmer type users as an entity"""

    def __init__(
            self,
            id: str,
            name: str,
            address: Address,
            email: str,
            password: str,
            orders: Optional[Sequence[Order]] = [],
            starredFarmers: Optional[Sequence[Farmer]] = []
    ):

        self.id: str = id,
        self.name: str = name,
        self.address: str = address,
        self.email: str = email,
        self.password: str = password,
        self.orders: Optional[Sequence[Order]] = orders,
        self.starredFarmers: Optional[Sequence[Farmer]] = starredFarmers

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Shopper):
            return self.id == o.id

        return False
