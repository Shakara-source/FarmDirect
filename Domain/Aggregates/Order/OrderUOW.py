from abc import ABC, abstractmethod
from IOrderRepository import OrderRepository


class OrderUnitOfWork(ABC):

    """Order UOW"""

    repository: OrderRepository

    @abstractmethod
    def begin(self):
        
        pass

    @abstractmethod
    def commit(self):
        
        pass

    @abstractmethod
    def rollback(self):
        
        pass