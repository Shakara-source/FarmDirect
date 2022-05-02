from Worker import app
from datetime import datetime
from Application.Models.OrderDTO import CardSchema, NewOrder
from Infrastructure.Services.MailGun import emailFactory


class PaymentTasks(app.Task):

    # Mocks a payment verification service such as stripe
    def calculatePrice(data: NewOrder):

        items = data.items
        totalCost = 0
        for item in items:
            totalCost += item.price * item.quantity

        return totalCost

    def verifyPayment(data: CardSchema):

        try:

            today = datetime.now()
            if len(
                data.cardNumber == 16
            ) and len(3 <= data.cvv <= 4) and data.expiration > today:

                return True

        except Exception:

            raise


class OrderTasks(app.Task):

    def sendInvoice(user, items):

        method = 'orderInvoice'
        template = 'temp'
        res = emailFactory(method, user, items, template)

        return res

    def sendFarmerNotification(farmer, user, items):

        method = 'orderNotification'
        template = 'temp'
        res = emailFactory(method, farmer, user, items, template)

        return res

    def orderEnroute(user, items):

        method = 'orderEnroute'
        template = 'temp'
        res = emailFactory(method, user, items, template)

        return res
