from py_dto import DTO
from typing import List


class ShopperAddressSchema(DTO):

    address: str
    city: str
    zipCode: int
    state: str


class FavoriteFarmersSchema(DTO):

    id: str


class ShopperBaseSchema(DTO):

    name: str
    email: str
    password: str
    address: ShopperAddressSchema
    favoriteFarmers: List[FavoriteFarmersSchema]
