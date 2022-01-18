from Seedwork.Application.Commands import Command

from Utilities.Address import Address
from Domain.Aggregates.Item.Item import Item
from typing import Set
from Domain.Aggregates.Farmer.Farmer import Farmer
from Domain.Aggregates.Shopper.Shopper import Shopper
from Infrastructure.Repositories import OrderRepo 
from Domain.Aggregates.Item.ItemCategories import Category
from Seedwork.Application.CommandHandlers import CommandResult
from Seedwork.Application.Decorators import command_handler


class CreateOrderCommand(Command):
    """A command for creating new user"""

    name: str
    shopperAddress: Shopper[Address]
    farmerAddress: Farmer[Address]
    items: Set[Item]

@command_handler
def CreateItem(
    command: CreateOrderCommand, repository: OrderRepo
) -> CommandResult:
    listing = Listing(id=repository.next_id(), **command.dict())
    try:
        repository.insert(listing)
    except Exception as e:
        return CommandResult.failed(message="Failed to create listing", exception=e)

    return CommandResult.ok(result=listing.id)

