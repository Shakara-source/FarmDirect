from py_dto import DTO


class FarmerAddressSchema(DTO):

    address: str
    city: str
    zipCode: int
    state: str


class FarmerBaseSchema(DTO):

    name: str
    email: str
    imageUrl: str
    password: str
    address: FarmerAddressSchema
