from abc import ABC, abstractmethod
from IFarmerRepository import FarmerRepository


class FarmerUnitOfWork(ABC):

    """Farmer UOW"""

    repository: FarmerRepository

    @abstractmethod
    def begin(self):
        
        pass

    @abstractmethod
    def commit(self):
        
        pass

    @abstractmethod
    def rollback(self):
        
        pass
