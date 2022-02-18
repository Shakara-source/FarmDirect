from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Item import Item
from Database import Base


class Order(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, nullable=False)
    items = relationship(f"{Item}", back_populates="order")
    
