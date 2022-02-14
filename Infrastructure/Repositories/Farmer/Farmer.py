from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Farmer(Base):

    __tablename__ = 'farmer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    # address 
    email = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    orders = relationship('Order', back_populates="farmer")
    inventory = relationship('Item', back_populates="farmer")
    
  