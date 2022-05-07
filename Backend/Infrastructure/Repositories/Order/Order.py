from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import backref, relationship
from typing import List
from Domain.Aggregates.Order import Order
from API.Application.Models.OrderReadModel import OrderReadModel
from Database import Base, mapper_registry


class OrderItem(Base):

    orderId = Column(ForeignKey(
        'order.id', ondelete="RESTRICT"), primary_key=True)
    itemId = Column(String, primary_key=True)
    farmerId = Column(String, primary_key=True)
    name = Column(String, primary_key=True)
    quantity = Column(Integer, primary_key=True)
    price = Column(Float, primary_key=True)


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
    def item_list(self, items: List):

        self.items = list(map(lambda item:
                              OrderItem(
                                  orderId=self.id, itemId=item['itemId'],
                                  itemName=item['name'],
                                  quantity=item['quantity'],
                                  farmerId=['farmerId'],
                                  price=item['price']), items))

    def to_entity(self) -> Order:

        return Order(
            id=self.id,
            status=self.status,
            total=self.total,
            shopper_id=self.shopper_id,
            items=list(map(lambda item: item, self.items))
        )

    def to_read_model(self) -> OrderReadModel:

        return OrderReadModel(
            id=self.id,
            status=self.status,
            total=self.total,
            shopper_id=self.shopper_id,
            items=list(map(lambda item: item, self.items))
        )

    @staticmethod
    def from_entity(order: Order) -> "OrderStore":
        return OrderStore(
            id=order.id,
            status=order.status,
            total=order.total,
            shopper_id=order.shopper_id,
            items=order.items
        )


def start_mapper():
    t = OrderStore.__table__
    rt = OrderItem.__table__

    mapper_registry.map_imperatively(Order, t, properties={
        'items': relationship(OrderItem,
                              backref=backref("order"), lazy='joined')
    })
    mapper_registry.map_imperatively(OrderItem, rt, properties={
        'order': relationship(Order,
                              backref=backref("author",
                                              cascade="all, delete-orphan"),
                              lazy='joined')
    })
