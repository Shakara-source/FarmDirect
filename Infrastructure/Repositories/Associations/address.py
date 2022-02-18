from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from Farmer import Farmer
from ValueObjects.Address import Address
from Database import Base


class FarmerAddress(Base):
    
    __tablename__ = 'farmerAddress'

    farmer_id = Column(ForeignKey(f"{Farmer}.id"), primary_key=True)
    address_id = Column(ForeignKey(f"{Address}.id"), primary_key=True)
    address = relationship(f"{Address}")
