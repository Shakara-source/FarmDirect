from Domain.Aggregates.Farmer.IFarmerRepository import FarmerRepository


class FarmerQueries:

    def getAllFarmers():

        farmers = FarmerRepository.findAll()
        return farmers
    
    def findById(farmerId: str):

        farmer = FarmerRepository.findById(farmerId)
        return farmer

    def findFarmerEmail(farmerId: str) -> str:

        email = FarmerRepoImplementation.findEmail(farmerId)
        return email


