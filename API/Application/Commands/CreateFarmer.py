# from seedwork.application.commands import Command
from Seedwork.Application.Commands import Command
from Domain.Aggregates.Farmer import Farmer
from Infrastructure.Repositories.Farmer import FarmerRepo 
from Seedwork.Application.CommandHandlers import CommandResult
from Seedwork.Application.Decorators import command_handler


class CreateFarmerCommand(Command):
    """A command for creating new user"""

    phoneNumber: str
    password: str


@command_handler
def CreateFarmer(
    command: CreateFarmerCommand, repository: FarmerRepo
) -> CommandResult:
    listing = Listing(id=repository.next_id(), **command.dict())
    try:
        repository.insert(listing)
    except Exception as e:
        return CommandResult.failed(message="Failed to create listing", exception=e)

    return CommandResult.ok(result=listing.id)
