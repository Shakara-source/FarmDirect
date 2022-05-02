from datetime import date
from pydantic import BaseModel


class PaymentInfo(BaseModel):
    
    """PaymentInfo represents farmer type users as an entity"""

    def __init__(
        self,
        cardNumber: str,
        expiration: date,
        cvv: str,
        shopperId: str,
    ):

        self.id: str = id,
        self.cardNumber: str = cardNumber,
        self.expiration: date = expiration
        self.cvv: str = cvv,
        self.shopperId: str = shopperId

    def __eq__(self, o: object) -> bool:
        if isinstance(o, PaymentInfo):
            return self.id == o.id

        return False
    
    