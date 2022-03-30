from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, eq=True, frozen=True)
class PaymentInfo:

    """paymentInfo represents payment information as a value object"""

    cardNumber: str
    expiration: datetime
    zipCode: int
    state: str
