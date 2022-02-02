from typing import Sequence, Optional
from Utilities.Address import Address
from Aggregates.Item.Item import Item
from Aggregates.Order.Order import Order
from Aggregates.Farmer.Farmer import Farmer
from ShoppingCart import Cart


class Shopper:
    """Farmer represents farmer type users as an entity"""

    def __init__(
            self,
            id: str,
            name: str,
            address: Address,
            email: str,
            phoneNumber: float,
            password: str,
            cart: Optional[Cart] = None,
            orders: Optional[Sequence[Order]] = [],
            starredFarmers: Optional[Sequence[Farmer]] = []
    ):

        self.id: str = id,
        self.name: str = name,
        self.address: str = address,
        self.email: str = email,
        self.phoneNumber: float = phoneNumber,
        self.password: str = password,
        self.cart: Optional[Sequence[Item]] = cart,
        self.orders: Optional[Sequence[Order]] = orders,
        self.starredFarmers: Optional[Sequence[Farmer]] = starredFarmers

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Shopper):
            return self.id == o.id

        return False
