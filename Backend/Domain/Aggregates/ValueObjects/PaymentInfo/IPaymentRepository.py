from abc import ABC, abstractmethod
from typing import List
from Payment import Payment


class PaymentRepository(ABC):
    """A repository interface for Payment entity."""

    @abstractmethod
    def findAll(self) -> List[Payment]:

        pass

    def findById(self, id: str) -> Payment:

        pass

    @abstractmethod
    def findByShopperId(self, shopperId: str) -> List[Payment]:

        pass

    @abstractmethod
    def update(self, payment: Payment) -> None:

        pass

    @abstractmethod
    def deleteById(self, id: str) -> None:

        pass
