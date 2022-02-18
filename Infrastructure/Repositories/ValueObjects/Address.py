from sqlalchemy import Column, Integer, String
from Database import Base


class Address(Base):

    __tablename__ = 'address'
    
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False),
    city = Column(String, nullable=False),
    zipCode = Column(Integer, nullable=False),
    state = Column(String, nullable=False)

