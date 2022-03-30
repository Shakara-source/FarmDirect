from sqlalchemy import Column, Integer, String, Float, ARRAY
from Database import Base


class Order(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, nullable=False)
    shopper_id = Column(Integer, index=True, nullable=False)
    address_ids = Column(ARRAY(Integer), index=True)
    total = Column(Float, index=True, nullable=False)
    
