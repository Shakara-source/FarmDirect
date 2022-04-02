from abc import ABC, abstractmethod
from typing import Optional, cast
import shortuuid

from Domain.Aggregates.Farmer import Farmer, FarmerRepository
from Models.FarmerDTO import FarmerAddressSchema, FarmerBaseSchema, FarmerLogin


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


class FarmerCommand(ABC):

    @abstractmethod
    def NewFarmer(self, data: FarmerBaseSchema) -> Farmer:
        pass
