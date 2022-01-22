from typing import Sequence, Optional
from Utilities.Address import Address
from Aggregates.Item.Item import Item
from Aggregates.Order.Order import Order


class Farmer:
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id: str,
        name: str,
        address: Address,
        email: str,
        phoneNumber: float,
        password: str,
        orders: Optional[Sequence[Order]] = [],
        inventory: Optional[Sequence[Item]] = []
    ):

        self.id: str = id,
        self.name: str = name,
        self.email: str = email,
        self.address: str = address,
        self.phoneNumber: float = phoneNumber,
        self.password: str = password,
        self.orders: Optional[Sequence[Order]] = orders,
        self.inventory: Optional[Sequence[Order]] = inventory

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Farmer):
            return self.id == o.id

        return False
