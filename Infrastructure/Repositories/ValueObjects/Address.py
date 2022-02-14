from sqlalchemy.ext.mutable import MutableComposite
from sqlalchemy import Column, Integer, String


class Address(MutableComposite):

    Column('Address', String, nullable=False),
    Column('City', String, nullable=False),
    Column('ZipCode', Integer, nullable=False),
    Column('State', String, nullable=False)
