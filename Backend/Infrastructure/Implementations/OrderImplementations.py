from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from Domain.Aggregates.Order import Order, OrderRepository, Status
from Repositories.Order import OrderStore


class OrderRepoImpl(OrderRepository):

    def __init__(self, session: Session):

        self.session: Session = session

    def findById(self, orderId: str) -> Order:

        try:

            order = self.session.query(
                OrderStore).filter_by(id=orderId).one()

        except NoResultFound:

            raise

        return order.to_entity()

    def create(self, order: Order):

        order = OrderStore.from_entity(order)
        try:

            self.session.add(order)

        except NoResultFound:

            raise

    def update(self, order: Order):

        order = OrderStore.from_entity(order)
        try:
            _Order = self.session.query(
                OrderStore).filter_by(id=order.id).one()
            _Order.name = order.name,
            _Order.imageUrl = order.imageUrl,
            _Order.email = order.imageUrl

        except NoResultFound:

            raise

    def findByShopperId(self, shopperId: str, status: Status) -> List[Order]:

        try:

            shopperOrders = self.session.query(
                OrderStore).filter_by(id=shopperId, status=status).all()

        except NoResultFound:

            raise

        return list(map(lambda order: order.to_entity(), shopperOrders))

    def deleteById(self, id: str):

        try:

            self.session.query(OrderStore).filter_by(id=id).delete()

        except NoResultFound:

            raise
