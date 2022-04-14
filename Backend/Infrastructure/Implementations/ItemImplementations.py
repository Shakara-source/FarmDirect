from typing import List
from sqlalchemy.orm.exc import NoResultFound

from sqlalchemy.orm.session import Session
from Domain.Aggregates.Item import Item, ItemRepository
from Repositories.Item import ItemStore


class ItemRepoImpl(ItemRepository):

    def __init__(self, session: Session):

        self.session: Session = session

    def findAll(self, number: int) -> List[Item]:
        try:

            items = (
                self.session.query(ItemStore).limit(number).all()
            )
        except NoResultFound:

            raise

        if len(items) == 0:
            return []

        return list(map(lambda item: item.to_entity(), items))

    def findById(self, itemId: str) -> Item:

        try:

            item = self.session.query(
                ItemStore).filter_by(id=itemId).one()

        except NoResultFound:

            raise

        return item.to_entity()

    def create(self, item: Item):

        item = ItemStore.from_entity(item)

        try:

            self.session.add(item)

        except NoResultFound:

            raise

    def update(self, item: Item):

        item = ItemStore.from_entity(item)
        try:
            _Item = self.session.query(
                ItemStore).filter_by(id=item.id).one()
            _Item.name = item.name,
            _Item.imageUrl = item.imageUrl,
            _Item.email = item.imageUrl

        except NoResultFound:

            raise

    def findItems(self, itemArray: List) -> List[Item]:

        try:

            items = self.session.query(ItemStore).filter_by(
                id.in_(itemArray)).group_by(ItemStore.farmer_id).all()

        except NoResultFound:

            raise

        return list(map(lambda item: item.to_entity(), items))

    def deleteById(self, id: str):

        try:

            self.session.query(ItemStore).filter_by(id=id).delete()

        except NoResultFound:

            raise
