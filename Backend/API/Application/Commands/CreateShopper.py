from pydantic import BaseModel
from Utilities.Address import Address
from Domain.Aggregates.Item.Item import Item
from Domain.Aggregates.Farmer.Farmer import Farmer
from Domain.Aggregates.Shopper.Shopper import Shopper


class CreateShopperCommand(BaseModel):
    """A command for creating new user"""

    shopperAdress: Shopper[Address]
    farmerAddress: Farmer[Address]
    items: list[Item]
