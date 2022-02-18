from sqlalchemy import Column, Integer, Date
from Database import Base


class PaymentInfo(Base):

    __tablename__ = 'paymentInfo'
    
    id = Column(Integer, primary_key=True)
    cardNumber = Column(Integer, primary_key=True)
    expiration = Column(Date, primary_key=True)
    cvv = Column(Integer, primary_key=True)


