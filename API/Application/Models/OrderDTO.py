from py_dto import DTO
from Domain.Utilities.Address import Address
from Domain.Aggregates.Shopper import Shopper
from Domain.Aggregates.Farmer import Farmer
from Domain.Aggregates.Item.Item import Item
from Domain.Aggregates.Order.OrderStatus import Status


class Order(DTO):

    shopper: Shopper
    farmer: Farmer
    items: list[Item]
    status: Status
