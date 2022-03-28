from pydantic import BaseModel
from ItemCategories import Category
from ItemStatus import Status


class Item(BaseModel):
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        name: str,
        description: str,
        image_url: str,
        price: float,
        category: Category,
        status: Status,
        farmer_id: int
    ):

        self.id: str = id,
        self.name: str = name,
        self.description: str = description,
        self.image_url: str = image_url
        self.price: float = price,
        self.category: str = category
        self.status: str = status,
        self.farmer_id: int = farmer_id,
        self.order_id: int = None

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Item):
            return self.id == o.id

        return False
