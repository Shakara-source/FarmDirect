from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database import Base
from farmerAddress import FarmerAddress
from favoriteFarmer import FavoriteFarmers


class Shopper(Base):

    __tablename__ = 'shopper'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=True, index=True)
    email = Column(String, primary_key=True, index=True)
    password = Column(String, primary_key=True, index=True)
    
    favoriteFarmers = relationship(f"{FavoriteFarmers}")
    address = relationship(f"{FarmerAddress}")
    
    def __repr__(self):
        
        return f"<Shopper {self.email}"

    
