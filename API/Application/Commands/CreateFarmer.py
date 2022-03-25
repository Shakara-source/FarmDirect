# from seedwork.application.commands import Command
from Seedwork.Application.Commands import Command
from Domain.Aggregates.Farmer import Farmer
from Infrastructure.Repositories.Farmer import FarmerRepo 
from Seedwork.Application.CommandHandlers import CommandResult
from Seedwork.Application.Decorators import command_handler


class FarmerCommands:

    def __init__(self) -> None:
        self._farmer_repository = 