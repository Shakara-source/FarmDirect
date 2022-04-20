from Domain.Aggregates.Order.IOrderRepository import OrderRepository


def OrderQuerySwitchboard(function: str, *args):

    if function == 'findAll':

        OrderQueries.findAll()

    if function == 'findById':

        OrderQueries.findById(args)

    if function == 'findByFarmerId':

        OrderQueries.findByFarmerId(args)

    if function == 'findByCategory':

        OrderQueries.findByCategory(args)

    if function == 'findByName':

        OrderQueries.findByName(args)

    if function == 'findMultipleItems':

        OrderQueries.findMultipleItems(args)


class OrderQueries:

    def findAll():

        result = OrderRepository.findAll()
        return result

    def findById(orderId: str):

        result = OrderRepository.findById(orderId)
        return result

    def findByShopperId(shopperId: str, status: str):

        result = OrderRepository.findByFarmerId(shopperId, status)
        return result

