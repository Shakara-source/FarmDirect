from abc import ABC, abstractmethod
from Models.OrderDTO import CardSchema
from Infrastructure.Services.Celery.Tasks import verifyCard


class VerifyCardCommandUseCase(ABC):

    @abstractmethod
    def verifyCard(self, data: CardSchema) -> str:

        raise NotImplementedError


class VerifyCardUseCaseImplementation(VerifyCardCommandUseCase):

    def verifyCard(self, data: CardSchema):
        paymentTask = verifyCard.delay(data)
        return paymentTask.id
