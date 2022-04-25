from abc import ABC, abstractmethod
from msilib.schema import Error
from typing import Optional, cast
import shortuuid

from Domain.Aggregates.Item import Item, ItemRepository
from Models.FarmerDTO import FarmerBaseSchema
from Models.FarmerRead import FarmerReadModel


class ItemUnitOfWork(ABC):

    """Farmer UOW"""

    item_repository: ItemRepository

    @abstractmethod
    def begin(self):

        pass

    @abstractmethod
    def commit(self):

        pass

    @abstractmethod
    def rollback(self):

        pass


class ItemCommandUseCase(ABC):

    @abstractmethod
    def create(self, data: ItemBaseSchema) -> Optional[ItemReadModel]:

        raise NotImplementedError

    @abstractmethod
    def update(self, name: str, farmerId: str,
               data: ItemBaseSchema) -> Optional[ItemReadModel]:

        raise NotImplementedError

    @abstractmethod
    def deleteByName(self, name: str, farmerId: str):

        raise NotImplementedError


class ItemCommandImpl(ItemCommandUseCase):

    def __init__(self, uow: ItemUnitOfWork):
        self.uow: ItemUnitOfWork = uow

    def create(self, data: ItemBaseSchema) -> Optional[FarmerReadModel]:
        
        try:
            uuid = shortuuid.uuid(),
            item = Item(id=uuid, name=data.name, imageUrl=data.imageUrl,
                            email=data.email, password=password)
            self.uow.item_repository.create(item)
            self.uow.commit()
            createdItem = self.uow.farmer_repository.findById(uuid)
            
            
        except Exception:

            self.uow.rollback()
            raise

        return ItemReadModel.from_entity(cast(Item, createdItem))

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
