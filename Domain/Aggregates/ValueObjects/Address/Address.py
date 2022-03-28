from pydantic import BaseModel


class Address(BaseModel):

    """Address represents address type users as an entity"""

    def __init__(
        self,
        address: str,
        city: str,
        zipCode: int,
        state: str,
    ):

        self.id: str = id,
        self.address: str = address,
        self.city: str = city
        self.zipCode: int = zipCode,
        self.state: str = state

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Address):
            return self.id == o.id

        return False
