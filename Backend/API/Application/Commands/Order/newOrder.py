from abc import ABC, abstractmethod
from Infrastructure.UOW.OrderUOW import OrderUnitOfWork
from Domain.Aggregates.Order import Order
from Models.OrderDTO import OrderBaseSchema
from Models.OrderReadModel import OrderReadModel
from Infrastructure.Services.Celery.Tasks import PaymentTasks, OrderTasks
import shortuuid


class NewOrderCommandUseCase(ABC):

    @abstractmethod
    def createNewOrder(self, data: OrderBaseSchema) -> Optional[OrderReadModel]:

        raise NotImplementedError


class NewOrderUseCaseImplementation(NewOrderCommandUseCase):

    def __init__(self, uow: OrderUnitOfWork):
        self.uow: OrderUnitOfWork = uow

    def createNewOrder(self, data: OrderBaseSchema) -> Optional[OrderReadModel]:

        try:

            PaymentTasks.verify(payment)
            Order.newOrder()
            createdItem = self.uow.farmer_repository.findById(uuid)

        except Exception:

            self.uow.rollback()
            raise

        return ItemReadModel.from_entity(cast(Item, createdItem))
