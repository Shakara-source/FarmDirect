from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database import Base
from farmerAddress import FarmerAddress


class Farmer(Base):

    __tablename__ = 'farmer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)

    address = relationship(f"{FarmerAddress}")

    def __repr__(self):

        return f"<Farmer {self.email}"
