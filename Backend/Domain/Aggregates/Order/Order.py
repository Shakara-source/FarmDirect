from OrderStatus import OrderStatus
from typing import List
from pydantic import BaseModel


class Order(BaseModel):

    """Order represents order type users as an entity"""

    def __init__(
        self,
        status: OrderStatus,
        shopper_id: int,
        total: float,
    ):

        self.id: str = id,
        self.status: OrderStatus = status,
        self.shopper_id: int = shopper_id,
        self.item_ids: List[int]
        self.total: float = total

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Order):
            return self.id == o.id

        return False

    def calculatePrice(self, itemArray: List) -> None:

        totalCost = 0
        for item in itemArray:
            totalCost += item['price']

        self.total = totalCost

    def removeItem(self, itemId: int) -> None:

        self.item_ids.remove(itemId)

    def updateStatus(self, newStatus: OrderStatus) -> None:

        self.status = newStatus

    def groupByFarmer(self, itemArray: List) -> List:

        response = {}
        arr_keys = response.keys()

        for item in itemArray:

            if item['farmer_id'] not in arr_keys:

                response['farmer_id'] = [item]

            else:

                response['farmer_id'].append(item)
        
        return response
