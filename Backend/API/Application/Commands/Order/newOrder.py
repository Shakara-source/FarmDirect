from abc import ABC, abstractmethod
from typing import Optional
from Infrastructure.UOW.OrderUOW import OrderUnitOfWork
from Domain.Aggregates.Order import Order
from Models.OrderDTO import NewOrderSchema
from Models.OrderReadModel import OrderReadModel
from Infrastructure.Services.Celery.Worker import app
from celery.result import AsyncResult


class NewOrderCommandUseCase(ABC):

    @abstractmethod
    def createNewOrder(self, data: NewOrderSchema) -> Optional[OrderReadModel]:

        raise NotImplementedError


class NewOrderUseCaseImplementation(NewOrderCommandUseCase):

    def __init__(self, uow: OrderUnitOfWork):
        self.uow: OrderUnitOfWork = uow

    def createNewOrder(self, cardId: str, data: NewOrderSchema) -> str:

        try:
            cardVerification = AsyncResult(cardId, app=app)
            result = cardVerification.ready()
            if result == 'SUCCESS':
                
                order = Order.newOrder(data)

        except Exception:

            self.uow.rollback()
            raise

        return order.Id
