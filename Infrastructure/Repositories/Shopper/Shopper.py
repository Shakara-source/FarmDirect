from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from Database import Base


class Shopper(Base):

    __tablename__ = 'shopper'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String(30), index=True)
    email = Column(String(30), index=True)
    password = Column(String(30), index=True)
    favorite_farmers_ids = Column(ARRAY(Integer), index=True)
    address_ids = Column(ARRAY(Integer), index=True)

    def __repr__(self):

        return f"<Shopper {self.email}"
