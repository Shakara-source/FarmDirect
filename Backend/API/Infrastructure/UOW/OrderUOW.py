from abc import ABC, abstractmethod
from Domain.Aggregates.Order import OrderRepository


class OrderUnitOfWork(ABC):

    """Farmer UOW"""

    order_repository: OrderRepository

    @abstractmethod
    def begin(self):

        pass

    @abstractmethod
    def commit(self):

        pass

    @abstractmethod
    def rollback(self):

        pass
