from abc import ABC, abstractmethod
from typing import List
from Address import Address


class AddressRepository(ABC):
    """A repository interface for Address entity."""

    @abstractmethod
    def findById(self, id: str) -> Address:

        pass

    @abstractmethod
    def findMultipleAddresses(self, itemIds: List[str]) -> List[Address]:

        pass

    @abstractmethod
    def update(self, Address: Address) -> None:

        pass

    @abstractmethod
    def deleteById(self, id: str) -> None:

        pass
