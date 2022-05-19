from abc import ABC, abstractmethod
from typing import Union
from Backend.API.Application.Models.OrderDTO import OrderInvoiceSchema, FarmerInvoiceSchema
from Models.OrderDTO import CardSchema
from Infrastructure.Services.Celery.Tasks import verifyCard


class CommandUseCase(ABC):

    @abstractmethod
    def orderNotification(self,
                          orderId: str) -> Union[OrderInvoiceSchema,
                                                 FarmerInvoiceSchema]:

        raise NotImplementedError


class CommandUseCaseImplementation(CommandUseCase):

    def verifyCard(self, data: CardSchema):
        paymentTask = verifyCard.delay(data)
        return paymentTask.id
