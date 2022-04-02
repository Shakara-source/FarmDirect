from Domain.Aggregates.Item.IItemRepository import ItemRepository


class FarmerQueries:

    def getAllItems():

        result = ItemRepository.findAll()
        return result
    
    def findById(itemId: str):

        result = ItemRepository.findById(itemId)
        return result
    
    def findByFarmerId(farmerId: str):

        result = ItemRepository.findByFarmerId(farmerId)
        return result
    
    def findByCategory(farmerId: str):

        result = ItemRepository.findByFarmerId(farmerId)
        return result



