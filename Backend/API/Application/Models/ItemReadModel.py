from pydantic import BaseModel

from Domain.Aggregates.Farmer import Farmer


class FarmerReadModel(BaseModel):

    """BookReadModel represents data structure as a read model."""

    id: str = '',
    name: str = '',
    imageUrl: str = '',
    email: str = ''

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(farmer: Farmer) -> "FarmerReadModel":
        return FarmerReadModel(
            id=farmer.id,
            name=farmer.name,
            imageUrl=farmer.imageUrl,
            email=farmer.email
        )
