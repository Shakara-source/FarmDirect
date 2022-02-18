from abc import ABC, abstractmethod
from typing import Optional, cast
from Domain.Aggregates.Farmer.IFarmerRepository import FarmerRepository

import shortuuid

from Domain.Aggregates.Order import (
    Order,
    IOrderRepository
)

from .book_command_model import BookCreateModel, BookUpdateModel
from .book_query_model import BookReadModel


class BookCommandUseCaseUnitOfWork(ABC):
    """BookCommandUseCaseUnitOfWork defines an interface based on UOW pattern."""

    farmer_repository: FarmerRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError
