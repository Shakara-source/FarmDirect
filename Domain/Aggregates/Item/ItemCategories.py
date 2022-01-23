from enum import Enum


class Category(str, Enum):
    Vegetables = 'Vegetables',
    Fruits = 'Fruits',
    Eggs = 'Eggs',
    Dairy = 'Dairy Products',
    Other = 'Other Treats'
