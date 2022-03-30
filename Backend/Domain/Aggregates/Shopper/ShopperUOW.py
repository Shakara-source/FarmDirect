from abc import ABC, abstractmethod
from IShopperRepository import ShopperRepository


class ShopperUnitOfWork(ABC):

    """Shopper UOW"""

    repository: ShopperRepository

    @abstractmethod
    def begin(self):
        
        pass

    @abstractmethod
    def commit(self):
        
        pass

    @abstractmethod
    def rollback(self):
        
        pass