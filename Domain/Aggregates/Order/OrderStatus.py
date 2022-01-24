from enum import Enum


class Status(str, Enum):
    
    Ordered = 'Ordered'
    Shipped = 'Shipped'
    Delivered = 'Delivered'
    
