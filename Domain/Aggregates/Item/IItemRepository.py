from abc import ABC, abstractmethod
from typing import Optional

from Item import Item


class ItemRepository(ABC):
    """A repository interface for Item entity."""

    @abstractmethod
    def create(self, Item: Item) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def findById(self, id: str) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def update(self, Item: Item) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def deleteById(self, id: str):
        raise NotImplementedError