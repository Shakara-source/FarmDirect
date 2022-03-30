from pydantic import BaseModel
from Utilities.Address import Address


class Farmer(BaseModel):
    
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id: str,
        name: str,
        address: Address,
        email: str,
        password: str,
    ):

        self.id: str = id,
        self.name: str = name,
        self.email: str = email,
        self.address: str = address,
        self.password: str = password,

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Farmer):
            return self.id == o.id

        return False
    
    
