from sqlalchemy import Column, Integer, String, Float
from Database import Base


class Item(Base):

    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    price = Column(Float, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    status = Column(String, index=True, nullable=False)
    farmer_id = Column(Integer, nullable=False)
    




