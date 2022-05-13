from abc import ABC, abstractmethod
from typing import Optional
from Infrastructure.UOW.OrderUOW import OrderUnitOfWork
from Domain.Aggregates.Order import Order
from Models.OrderDTO import NewOrderSchema
from Models.OrderReadModel import OrderReadModel
from Infrastructure.Services.Celery.Tasks import PaymentTasks, OrderTasks
import shortuuid


class NewOrderCommandUseCase(ABC):

    @abstractmethod
    def createNewOrder(self, data: NewOrderSchema) -> Optional[OrderReadModel]:

        raise NotImplementedError


class NewOrderUseCaseImplementation(NewOrderCommandUseCase):

    def __init__(self, uow: OrderUnitOfWork):
        self.uow: OrderUnitOfWork = uow

    def createNewOrder(self, data: NewOrderSchema) -> Optional[OrderReadModel]:

        try:

            await PaymentTasks.verifyPayment(data.payment)
            Order.newOrder(data)
            createdOrder = self.uow.farmer_repository.findById(uuid)
            OrderTasks.sendFarmerNotification()
            OrderTasks.sendInvoice()

        except Exception:

            self.uow.rollback()
            raise

        return OrderReadModel.from_entity(cast(Order, createdOrder))
