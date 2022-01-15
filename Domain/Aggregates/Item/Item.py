from ItemCategories import Category


class Item:
    """Farmer represents farmer type users as an entity"""

    def __init__(
        self,
        id:int,
        name:str,
        description:str, 
        price: float,
        category: Category 
        ):
        
        self.id: str = id,
        self.name: str = name,
        self.description: str = description,
        self.price: float = price,
        self.category: str = category
        

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Item):
            return self.id == o.id

        return False

