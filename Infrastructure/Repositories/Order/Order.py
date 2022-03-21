from sqlalchemy import Column, Integer, String
from Database import Base


class Order(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, primary_key=True, index=True)
    shopper_id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, nullable=False)
    
