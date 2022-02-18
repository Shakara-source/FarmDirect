from ItemCategories import Category
from ItemStatus import Status
from Aggregates.Farmer import Farmer


class Item:
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id: int,
        farmer: Farmer,
        name: str,
        description: str,
        price: float,
        category: Category,
        status: Status
    ):

        self.id: str = id,
        self.farmer: Farmer = farmer
        self.name: str = name,
        self.description: str = description,
        self.price: float = price,
        self.category: str = category
        self.status: str = status

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Item):
            return self.id == o.id

        return False
