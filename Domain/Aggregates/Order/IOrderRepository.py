from abc import ABC, abstractmethod
from typing import Optional

from Domain.Aggregates.Farmer import Farmer


class FarmerRepository(ABC):
    """A repository interface for Farmer entity."""

    @abstractmethod
    def create(self, farmer: Farmer) -> None:
        raise NotImplementedError

    @abstractmethod
    def findById(self, id: str) -> Optional[Farmer]:
        raise NotImplementedError

    @abstractmethod
    def update(self, farmer: Farmer) -> None:
        raise NotImplementedError

    @abstractmethod
    def deleteById(self, id: str):
        raise NotImplementedError
