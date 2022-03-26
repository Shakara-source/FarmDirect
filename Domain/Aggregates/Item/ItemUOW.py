from abc import ABC, abstractmethod
from IItemRepository import ItemRepository


class ItemUnitOfWork(ABC):

    """Item UOW"""

    repository: ItemRepository

    @abstractmethod
    def begin(self):
        
        pass

    @abstractmethod
    def commit(self):
        
        pass

    @abstractmethod
    def rollback(self):
        
        pass