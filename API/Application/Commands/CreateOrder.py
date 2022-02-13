
from pydantic import BaseModel, Field, validator
from Utilities.Address import Address
from Domain.Aggregates import Farmer, Shopper, Item
from Infrastructure.Services.Celery import add
from Application.Models import OrderDTO


class CreateOrderCommand(BaseModel):
    """A command for creating new user"""

    shopperAddress: Address
    farmerAddress: Address
    items: list[Item]

