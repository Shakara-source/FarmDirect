from abc import ABC, abstractmethod
from typing import List
from Item import Item


class ItemRepository(ABC):
    """A repository interface for Item entity."""

    @abstractmethod
    def findAll(self) -> List[Item]:

        pass

    @abstractmethod
    def findById(self, id: str) -> Item:

        pass

    @abstractmethod
    def findByFarmerId(self, farmerId: str) -> List[Item]:

        pass

    @abstractmethod
    def findByCategory(self, category: str) -> List[Item]:

        pass

    @abstractmethod
    def findByName(self, name: str) -> List[Item]:

        pass

    @abstractmethod
    def findByOrder(self, orderId: str) -> List[Item]:

        pass

    @abstractmethod
    def update(self, item: Item) -> None:

        pass

    @abstractmethod
    def deleteById(self, id: str) -> None:

        pass
