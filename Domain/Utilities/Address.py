from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class Address:

    """Address represents an address as a value object"""

    name: str
    address: str
    city: str
    zipCode: int
