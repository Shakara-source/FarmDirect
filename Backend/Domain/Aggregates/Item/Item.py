import uuid
from pydantic import BaseModel
from ItemCategories import Category


class Item(BaseModel):
    """Item represents item type users as an entity"""

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        image_url: str,
        price: float,
        category: Category,
        quantity: int,
        farmer_id: int
    ):

        self.id: uuid = id,
        self.name: str = name,
        self.description: str = description,
        self.image_url: str = image_url
        self.price: float = price,
        self.category: str = category,
        self.quantity: str = quantity,
        self.farmer_id: int = farmer_id

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Item):
            return self.id == o.id

        return False
