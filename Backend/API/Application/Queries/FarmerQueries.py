from Domain.Aggregates.Farmer.IFarmerRepository import FarmerRepository


class FarmerQueries:

    def getAllFarmers():

        farmers = FarmerRepository.findAll()
        return farmers
    
    def findById(farmerId: str):

        farmer = FarmerRepository.findById(farmerId)
        return farmer
