from datetime import datetime
from typing import Union

from sqlalchemy import Column, Integer, String, relationship

from Domain.Aggregates.Cart import Cart
from Infrastructure.Repositories.Database import Base
from dddpy.usecase.book import BookReadModel


class CartDTO(Base):
    """CartDTO is a data transfer object associated with Cart entity."""

    __tablename__ = "cart"
    id: Union[str, Column] = Column(
        String, primary_key=True, autoincrement=False)
    shopper: Union[str, Column] = Column(String(17), unique=True, nullable=False)
    shopperId: Union[str, Column] = Column(String, nullable=False)
    items: Union[int, Column] = Column(Integer, nullable=False)
    
    def to_entity(self) -> Book:
        return Book(
            id=self.id,
            isbn=Isbn(self.isbn),
            title=self.title,
            page=self.page,
            read_page=self.read_page,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def to_read_model(self) -> BookReadModel:
        return BookReadModel(
            id=self.id,
            isbn=self.isbn,
            title=self.title,
            page=self.page,
            read_page=self.read_page,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(book: Book) -> "BookDTO":
        now = unixtimestamp()
        return BookDTO(
            id=book.id,
            isbn=book.isbn.value,
            title=book.title,
            page=book.page,
            read_page=book.read_page,
            created_at=now,
            updated_at=now,
        )
