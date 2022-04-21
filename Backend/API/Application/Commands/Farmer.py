from abc import ABC, abstractmethod
from msilib.schema import Error
from typing import Optional, cast
import shortuuid

from Backend.Infrastructure.Config.hashing import Hashing
from Domain.Aggregates.Farmer import Farmer, FarmerRepository
from Models.FarmerDTO import FarmerBaseSchema
from Models.FarmerRead import FarmerReadModel


class FarmerUnitOfWork(ABC):

    """Farmer UOW"""

    farmer_repository: FarmerRepository

    @abstractmethod
    def begin(self):

        pass

    @abstractmethod
    def commit(self):

        pass

    @abstractmethod
    def rollback(self):

        pass


class FarmerCommandUseCase(ABC):

    @abstractmethod
    def create(self, data: FarmerBaseSchema) -> Optional[FarmerReadModel]:

        raise NotImplementedError

    @abstractmethod
    def update(self, id: str,
               data: FarmerBaseSchema) -> Optional[FarmerReadModel]:

        raise NotImplementedError

    @abstractmethod
    def deleteById(self, id: str):

        raise NotImplementedError


class FarmerCommandImpl(FarmerCommandUseCase):

    def __init__(self, uow: FarmerUnitOfWork):
        self.uow: FarmerUnitOfWork = uow

    def create(self, data: FarmerBaseSchema) -> Optional[FarmerReadModel]:

        try:
            uuid = shortuuid.uuid(),
            password = Hashing.bcrypt(data.password)
            farmer = Farmer(id=uuid, name=data.name, imageUrl=data.imageUrl,
                            email=data.email, password=password)

            existingFarmer = self.uow.farmer_repository.email(data.email)

            if existingFarmer is not None:

                raise Error

            self.uow.farmer_repository.create(farmer)
            self.uow.commit()

            createdFarmer = self.uow.farmer_repository.findById(uuid)

        except Exception:

            self.uow.rollback()
            raise

        return FarmerReadModel.from_entity(cast(Farmer, createdFarmer))

    def update(self, id: str,
               data: FarmerBaseSchema) -> Optional[FarmerReadModel]:

        try:

            ExistingFarmer = self.uow.farmer_repository.findById(id)

            if ExistingFarmer is None:

                raise Error

            farmer = Farmer(id=id, name=data.name,
                            imageUrl=data.imageUrl, email=data.email)

            self.uow.farmer_repository.update(farmer)

            updatedFarmer = self.uow.farmer_repository.findById(farmer.id)

            self.uow.commit()

        except Exception:

            self.uow.rollback()
            raise

        return FarmerReadModel.from_entity(cast(Farmer, updatedFarmer))

    def deleteById(self, id: str):

        try:
            ExistingFarmer = self.uow.farmer_repository.findById(id)

            if ExistingFarmer is None:

                raise Error

            self.uow.farmer_repository.deleteById(id)

            self.uow.commit()

        except Exception:

            self.uow.rollback()
            raise
