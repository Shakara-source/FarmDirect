from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Associations.address import FarmerAddress
from Associations.farmerOrders import FarmerOrder
from Associations.farmerItems import FarmerItem

from Database import Base


class Farmer(Base):

    __tablename__ = 'farmer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    address = relationship(f"{FarmerAddress}") 
    orders = relationship(f"{FarmerOrder}", back_populates="farmer")
    inventory = relationship(f"{FarmerItem}", back_populates="farmer")
    
