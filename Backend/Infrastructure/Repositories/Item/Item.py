from sqlalchemy import Column, Integer, String, Float
from Domain.Aggregates.Item import Item
from Database import Base


class ItemStore(Base):

    __tablename__ = 'item'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    imageUrl = Column(String, index=True, nullable=False)
    price = Column(Float, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    quantity = Column(Integer, index=True, nullable=False)
    farmer_id = Column(Integer, nullable=False)

    def to_entity(self) -> Item:

        return ItemStore(
            id=self.id,
            name=self.name,
            description=self.description,
            imageUrl=self.imageUrl,
            price=self.price,
            category=self.category,
            quantity=self.quantity,
            farmer_id=self.farmer_id
        )

    @staticmethod
    def from_entity(item: Item) -> "ItemStore":
        return ItemStore(
            id=item.id,
            name=item.name,
            description=item.description,
            imageUrl=item.imageUrl,
            price=item.price,
            category=item.category,
            quantity=item.quantity,
            farmer_id=item.farmer_id
        )
