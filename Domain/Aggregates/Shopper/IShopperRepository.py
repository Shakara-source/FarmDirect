from abc import ABC, abstractmethod
from typing import Optional

from Shopper import Shopper


class ShopperRepository(ABC):
    """A repository interface for Shopper entity."""

    @abstractmethod
    def create(self, Shopper: Shopper) -> Optional[Shopper]:
        raise NotImplementedError

    @abstractmethod
    def findById(self, id: str) -> Optional[Shopper]:
        raise NotImplementedError

    @abstractmethod
    def update(self, Shopper: Shopper) -> Optional[Shopper]:
        raise NotImplementedError

    @abstractmethod
    def deleteById(self, id: str):
        raise NotImplementedError