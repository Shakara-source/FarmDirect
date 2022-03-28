from typing import List
from ValueObjects.Address import Address
from pydantic import BaseModel


class Shopper(BaseModel):
    """Farmer represents farmer type users as an entity"""

    def __init__(
            self,
            name: str,
            email: str,
            password: str,
    ):

        self.id: str = id,
        self.name: str = name,
        self.email: str = email,
        self.password: str = password,
        self.favoriteFarmersId: List[int] = []
        self.addressIds = List[int] = []

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Shopper):
            return self.id == o.id

        return False

    def favoriteAFarmer(self, farmerId: int) -> None:

        return self.favoriteFarmersId.append(farmerId)

    def newAddress(self, address: str, city: str,
                   zipcode: int, state: str) -> None:

        NewAddress = Address(address, city, zipcode, state)
        id_ = NewAddress.id
        return self.addressIds.append(id_)
