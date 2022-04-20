from abc import ABC, abstractmethod
from typing import List
from Farmer import Farmer


class FarmerRepository(ABC):

    """A repository interface for Farmer entity."""

    @abstractmethod
    def findAll(self) -> List[Farmer]:

        pass

    @abstractmethod
    def findById(self, farmerId: str) -> Farmer:

        pass

    @abstractmethod
    def create(self, farmer: Farmer) -> Farmer:

        pass

    @abstractmethod
    def update(self, farmer: Farmer) -> None:

        pass

    @abstractmethod
    def deleteById(self, id: str) -> None:

        pass
