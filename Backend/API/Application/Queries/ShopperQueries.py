from Domain.Aggregates.Shopper.IShopperRepository import ShopperRepository


class ShopperQueries:

    def getAllShoppers():

        result = ShopperRepository.findAll()
        return result

    def findById(shopperId: str):

        result = ShopperRepository.findById(shopperId)
        return result

    def findByEmail(shopperEmail: str):

        result = ShopperRepository.findByFarmerId(shopperEmail)
        return result

