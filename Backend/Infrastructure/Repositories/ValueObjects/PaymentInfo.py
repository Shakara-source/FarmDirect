from sqlalchemy import Column, Integer, Date
from Database import Base


class PaymentInfo(Base):

    __tablename__ = 'paymentInfo'
    
    id = Column(Integer, primary_key=True)
    cardNumber = Column(Integer, index=True, nullable=False)
    expiration = Column(Date, index=True, nullable=False)
    cvv = Column(Integer, index=True, nullable=False)
    shopper_id = Column(Integer, index=True, nullable=False)


