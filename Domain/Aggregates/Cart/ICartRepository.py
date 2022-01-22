from abc import ABC, abstractmethod
from typing import Optional
from Aggregates.Item.Item import Item


class CartRepository(ABC):
    """A repository interface for cart entity."""

    @abstractmethod
    def addToCart(self, item: Item) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def removeFromCart(self, item: Item) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def clearCart(self, id: str):
        raise NotImplementedError
