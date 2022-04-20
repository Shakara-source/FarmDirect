from Domain.Aggregates.Item.IItemRepository import ItemRepository


def ItemQuerySwitchboard(function: str, *args):

    if function == 'findAll':

        ItemQueries.getAllItems()

    if function == 'findById':

        ItemQueries.findById(args)

    if function == 'findByFarmerId':

        ItemQueries.findByFarmerId(args)

    if function == 'findByCategory':

        ItemQueries.findByCategory(args)

    if function == 'findByName':

        ItemQueries.findByName(args)

    if function == 'findMultipleItems':

        ItemQueries.findMultipleItems(args)


class ItemQueries:

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
