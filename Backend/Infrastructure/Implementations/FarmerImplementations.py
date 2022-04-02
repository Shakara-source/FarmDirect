from typing import List
from sqlalchemy.orm.exc import NoResultFound

from sqlalchemy.orm.session import Session
from Domain.Aggregates.Farmer import Farmer, FarmerRepository
from Repositories.Farmer.Farmer import FarmerStore


class FarmerRepoImpl(FarmerRepository):

    def __init__(self, session: Session):

        self.session: Session = session

    def findAll(self, number: int) -> List[Farmer]:
        try:

            farmers = (
                self.session.query(FarmerStore).limit(number).all()
            )
        except NoResultFound:
            
            raise

        if len(farmers) == 0:
            return []

        return list(map(lambda farmer: farmer.to_entity(), farmers))

    def findById(self, farmerId: str) -> Farmer:

        try:

            farmer = self.session.query(
                FarmerStore).filter_by(farmerId=id).one()

        except NoResultFound:

            raise

        return farmer.to_entity()

    def create(self, farmer: Farmer):

        farmer = FarmerStore.from_entity(farmer)
        try:

            self.session.add(farmer)

        except NoResultFound:

            raise

    def update(self, farmer: Farmer):

        farmer = FarmerStore.from_entity(farmer)
        try:
            _Farmer = self.session.query(
                FarmerStore).filter_by(id=farmer.id).one()
            _Farmer.name = farmer.name,
            _Farmer.imageUrl = farmer.imageUrl,
            _Farmer.email = farmer.imageUrl

        except NoResultFound:

            raise

    def deleteById(self, id: str):

        try:

            self.session.query(FarmerStore).filter_by(id=id).delete()

        except NoResultFound:

            raise
