from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from Database import Base
from Farmer import Farmer
from Item import Item


class FarmerItem(Base):
    
    __tablename__ = 'farmerItem'

    farmer_id = Column(ForeignKey(f"{Farmer}.id"), primary_key=True)
    item_id = Column(ForeignKey(f"{Item}.id"), primary_key=True)
    item = relationship(f"{Item}")
