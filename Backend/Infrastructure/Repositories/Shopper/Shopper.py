from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from Domain.Aggregates.Shopper import Shopper
from Database import Base


class ShopperStore(Base):

    __tablename__ = 'shopper'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String(30), index=True)
    email = Column(String(30), index=True)
    password = Column(String(30), index=True)
    favorite_farmers_ids = Column(ARRAY(Integer), index=True)
    address_ids = Column(ARRAY(Integer), index=True)

    def to_entity(self) -> Shopper:

        return ShopperStore(
            id=self.id,
            name=self.name,
            imageUrl=self.imageUrl,
            email=self.email,
            password=self.password
        )

    @staticmethod
    def from_entity(shopper: Shopper) -> "ShopperStore":
        return ShopperStore(
            id=shopper.id,
            name=shopper.name,
            imageUrl=shopper.imageUrl,
            email=shopper.email
        )


    