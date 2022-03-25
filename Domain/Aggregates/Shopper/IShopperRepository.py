from abc import ABC, abstractmethod
from typing import List

from Shopper import Shopper


class ShopperRepository(ABC):
    """A repository interface for Shopper entity."""

    @abstractmethod
    def findAll(self) -> List[Shopper]:

        pass

    @abstractmethod
    def findById(self, id: str) -> Shopper:

        pass

    @abstractmethod
    def findByEmail(self, email: str) -> Shopper:

        pass

    @abstractmethod
    def update(self, shopper: Shopper) -> None:

        pass

    @abstractmethod
    def deleteById(self, id: str) -> None:

        pass
