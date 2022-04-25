from pydantic import BaseModel

from Domain.Aggregates.Shopper import Shopper


class ShopperReadModel(BaseModel):

    """ShopperReadModel represents data structure as a read model."""

    id: str = '',
    name: str = '',
    imageUrl: str = '',
    email: str = ''

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(farmer: Shopper) -> "ShopperReadModel":
        return ShopperReadModel(
            id=farmer.id,
            name=farmer.name,
            imageUrl=farmer.imageUrl,
            email=farmer.email
        )
