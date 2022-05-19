from OrderStatus import OrderStatus
from typing import List
from Aggregates.ValueObjects import Address, PaymentInfo
from pydantic import BaseModel
from OrderItems import OrderItems
from API.Application.Models.OrderDTO import NewOrderSchema
import shortuuid


class Order(BaseModel):

    """Order represents order type as an entity"""

    def __init__(
        self,
        id: str,
        status: OrderStatus,
        shopper_id: int,
        order_address: Address,
        payment_info: PaymentInfo,
        items: List[OrderItems]

    ):

        self.id: str = id,
        self.status: OrderStatus = status,
        self.shopper_id: str = shopper_id,
        self.order_address: Address = order_address,
        self.payment_info: PaymentInfo = payment_info,
        self.items: List[OrderItems] = items,
        self.total: float = 0.0

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Order):
            return self.id == o.id

        return False

    def newOrder(self, NewOrder: NewOrderSchema) -> 'Order':

        orderId = shortuuid.uuid()
        orderItems = list(map(lambda item: OrderItems(
            orderId=orderId, itemId=item.itemId,
            farmerId=item.farmerId, price=item.price,
            quantity=item.quantity
        )), NewOrder.items)

        total = self.calculatePrice(orderItems)

        return Order(id=orderId, shopper_id=NewOrder.shopper_id,
                     items=orderItems, total=total)

    def calculatePrice(self, items: List) -> None:

        totalCost = 0
        for item in items:
            totalCost += item['price'] * item['quantity']

        return totalCost

    def removeItem(self, itemId: int) -> None:

        self.item_ids.remove(itemId)

    def updateStatus(self, newStatus: OrderStatus) -> None:

        self.status = newStatus

    def groupOrderByFarmer(self, items: List[NewOrderSchema.items]) -> List:

        response = {}
        arr_keys = response.keys()

        for item in items:

            if item['farmer_id'] not in arr_keys:

                response['farmer_id'] = [item]

            else:

                response['farmer_id'].append(item)

        return response
