from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from Database import Base
from Item import Item
from Order import Order


class ItemOrder(Base):
    
    __tablename__ = 'itemOrder'

    order_id = Column(ForeignKey(f"{Order}.id"), primary_key=True)
    item_id = Column(ForeignKey(f"{Item}.id"), primary_key=True)
    item = relationship(f"{Item}")
