from sqlalchemy import Column, Integer, String, Float
from Domain.Aggregates.Order import Order
from Database import Base


class OrderStore(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, nullable=False)
    shopper_id = Column(Integer, index=True, nullable=False)
    shipping_address_id = Column(Integer, index=True, nullable=False)
    total = Column(Float, index=True, nullable=False)

    def to_entity(self) -> Order:

        return OrderStore(
            id=self.id,
            status=self.status,
            shopper_id=self.shopper_id,
            shipping_address_id=self.origin_address_id,
            total=self.total
        )

    @staticmethod
    def from_entity(order: Order) -> "OrderStore":
        return OrderStore(
            id=order.id,
            status=order.status,
            shopper_id=order.shopper_id,
            shipping_address_id=order.origin_address_id,
            total=order.total
        )
