from typing import Optional, List
from Utilities.Address import Address


class Order:
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id:str,
        name:str,
        address: Address, 
        password: str,
        openOrders: Optional[str],
        completedOrders: Optional[str],
        inventory: Optional[str]
        ):
        
        self.id: str = id,
        self.name: str = name,
        self.address: str = address,
        self.password: str = password,
        self.openOrders: list[str] = openOrders,
        self.completedOrders: list[str] = completedOrders,
        self.inventory: list[str] = inventory

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Order):
            return self.id == o.id

        return False

