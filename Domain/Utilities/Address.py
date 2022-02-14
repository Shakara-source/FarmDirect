from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class Address:

    """Address represents an address as a value object"""

    address: str
    city: str
    zipCode: int
    state: str
