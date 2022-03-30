from Seedwork.Application.Commands import Command
from Domain.Aggregates.Item import Item
from Infrastructure.Repositories import ItemRepo 
from Domain.Aggregates.Item.ItemCategories import Category
from Seedwork.Application.CommandHandlers import CommandResult
from Seedwork.Application.Decorators import command_handler


class CreateItemCommand(Command):
    """A command for creating new user"""

    name: str
    description: str
    price: float
    category: Category


@command_handler
def CreateItem(
    command: CreateItemCommand, repository: ItemRepo
) -> CommandResult:
    listing = Listing(id=repository.next_id(), **command.dict())
    try:
        repository.insert(listing)
    except Exception as e:
        return CommandResult.failed(message="Failed to create listing", exception=e)

    return CommandResult.ok(result=listing.id)
