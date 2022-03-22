from sqlalchemy import Column, Integer, String, Float
from Database import Base


class Order(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, nullable=False)
    total = Column(Float, index=True, nullable=False)
    
