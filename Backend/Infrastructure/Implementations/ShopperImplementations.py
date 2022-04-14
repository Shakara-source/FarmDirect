from typing import List
from sqlalchemy.orm.exc import NoResultFound

from sqlalchemy.orm.session import Session
from Domain.Aggregates.Shopper import Shopper, ShopperRepository
from Repositories.Shopper import ShopperStore


class ShopperRepoImpl(ShopperRepository):

    def __init__(self, session: Session):

        self.session: Session = session

    def findAll(self, number: int) -> List[Shopper]:
        try:

            shoppers = (
                self.session.query(ShopperStore).limit(number).all()
            )
        except NoResultFound:

            raise

        if len(shoppers) == 0:
            return []

        return list(map(lambda shopper: shopper.to_entity(), shoppers))

    def findById(self, shopperId: str) -> Shopper:

        try:

            shopper = self.session.query(
                ShopperStore).filter_by(id=shopperId).one()

        except NoResultFound:

            raise

        return shopper.to_entity()

    def create(self, shopper: Shopper):

        shopper = ShopperStore.from_entity(shopper)

        try:

            self.session.add(shopper)

        except NoResultFound:

            raise

    def update(self, shopper: Shopper):

        shopper = ShopperStore.from_entity(shopper)
        try:
            _Shopper = self.session.query(
                ShopperStore).filter_by(id=shopper.id).one()
            _Shopper.name = shopper.name,
            _Shopper.imageUrl = shopper.imageUrl,
            _Shopper.email = shopper.imageUrl

        except NoResultFound:

            raise

    def findShoppers(self, shopperArray: List) -> List[Shopper]:

        try:

            shopper = self.session.query(ShopperStore).filter_by(
                id.in_(ShopperArray)).group_by(ShopperStore.farmer_id).all()

        except NoResultFound:

            raise

        return list(map(lambda shopper: shopper.to_entity(), shoppers))

    def deleteById(self, id: str):

        try:

            self.session.query(ShopperStore).filter_by(id=id).delete()

        except NoResultFound:

            raise
