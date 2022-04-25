from dataclasses import dataclass
from sqlalchemy.ext.associationproxy import association_proxy
from typing import FrozenSet


@dataclass
class OrderDTO:
    id: str
    status: str
    shopper_id: str
    total: float
    items: FrozenSet[str] = association_proxy("order_items", "item_id")
