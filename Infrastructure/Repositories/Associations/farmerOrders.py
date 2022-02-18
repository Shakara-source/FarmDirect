from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from Database import Base
from Farmer import Farmer
from Order import Order


class FarmerOrder(Base):
    
    __tablename__ = 'farmerOrder'

    farmer_id = Column(ForeignKey(f"{Farmer}.id"), primary_key=True)
    order_id = Column(ForeignKey(f"{Order}.id"), primary_key=True)
    order = relationship(f"{Order}")
