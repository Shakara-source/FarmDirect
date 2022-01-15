from typing import Optional, Set
from Utilities.Address import Address
from Aggregates.Item.Item import Item
from Aggregates.Order.Order import Order


class Farmer:
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id:str,
        name:str,
        address: Address, 
        password: str
        ):
        
        self.id: str = id,
        self.name: str = name,
        self.address: str = address,
        self.password: str = password,
        self.openOrders: Set[Order] = [],
        self.completedOrders: Set[Order] = [],
        self.inventory: Set[Item] = []

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Farmer):
            return self.id == o.id

        return False


