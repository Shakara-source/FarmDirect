from sqlalchemy import Column, String, Integer, ARRAY
from Domain.Aggregates.Farmer import Farmer
from Database import Base


class FarmerStore(Base):

    __tablename__ = 'farmerstore'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    imageUrl = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    address_ids = Column(ARRAY(Integer), index=True)

    def to_entity(self) -> Farmer:

        return FarmerStore(
            id=self.id,
            name=self.name,
            imageUrl=self.imageUrl,
            email=self.email,
            password=self.password
        )

    @staticmethod
    def from_entity(farmer: Farmer) -> "FarmerStore":
        return FarmerStore(
            id=farmer.id,
            name=farmer.name,
            imageUrl=farmer.imageUrl,
            email=farmer.email
        )
