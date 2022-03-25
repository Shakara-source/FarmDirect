from abc import ABC, abstractmethod
from typing import List
from Order import Order


class OrderRepository(ABC):
    """A repository interface for Order entity."""

    @abstractmethod
    def findAll(self) -> List[Order]:

        pass

    @abstractmethod
    def findById(self, id: str) -> Order:

        pass

    @abstractmethod
    def findByShopperId(self, shopperId: str) -> List[Order]:

        pass

    @abstractmethod
    def findByStatus(self, status: str) -> List[Order]:

        pass

    @abstractmethod
    def update(self, order: Order) -> None:

        pass

    @abstractmethod
    def deleteById(self, id: str) -> None:

        pass
