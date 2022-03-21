from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from Farmer import Farmer
from Shopper import Shopper
from ValueObjects.Address import Address
from Database import Base


class FavoriteFarmers(Base):

    __tablename__ = 'favoriteFarmers'

    shopper_id = Column(ForeignKey(f"{Shopper}.id"), primary_key=True)
    farmer_id = Column(ForeignKey(f"{Farmer}.id"), primary_key=True)
    farmer = relationship(f"{Address}")
