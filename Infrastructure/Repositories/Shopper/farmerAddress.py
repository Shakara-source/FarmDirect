from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from Shopper import Shopper
from ValueObjects.Address import Address
from Database import Base


class ShopperAddress(Base):
    
    __tablename__ = 'farmerAddress'

    shopper_id = Column(ForeignKey(f"{Shopper}.id"), primary_key=True)
    address_id = Column(ForeignKey(f"{Address}.id"), primary_key=True)
    address = relationship(f"{Address}")
