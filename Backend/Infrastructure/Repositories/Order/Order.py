from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from typing import List
from Domain.Aggregates.Order import Order
from Database import Base


class OrderItem(Base):

    orderId = Column(ForeignKey(
        'order.id', ondelete="RESTRICT"), primary_key=True)
    itemId = Column(String, primary_key=True)
    quantity = Column(Integer, primary_key=True)


class OrderStore(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, nullable=False)
    total = Column(Float, index=True, nullable=False)
    shopper_id = Column(Integer, primary_key=True, index=True)

    # Mapped relationships
    items = relationship(OrderItem, viewonly=True, lazy='joined')

    @property
    def item_list(self) -> List[OrderItem]:

        return self.items

    @item_list.setter
    def item_list(self, items: list[int]):

        self.items = list(map(lambda _id, _quantity: OrderItem(
            OrderId=self.id, itemId=_id, quantity=_quantity), items))

    def to_entity(self) -> Order:

        return OrderStore(
            id=self.id,
            status=self.status,
            shopper_id=self.shopper_id,
            total=self.total
        )

    @staticmethod
    def from_entity(order: Order) -> "OrderStore":
        return OrderStore(
            id=order.id,
            status=order.status,
            shopper_id=order.shopper_id,
            total=order.total
        )
