from py_dto import DTO
from Domain.Utilities.Address import Address
from Domain.Aggregates.Item.Item import Item
from Domain.Aggregates.Order.OrderStatus import Status


class Farmer(DTO):

    shopperAddress: Address
    farmerAddress: Address
    items: list[Item]
    status: Status
