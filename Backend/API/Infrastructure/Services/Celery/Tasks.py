from Worker import app
from datetime import datetime
from Infrastructure.Services.MailGun import emailFactory, send_email


class Payments(app.Task):

    # Mocks a payment verification service such as stripe

    def verify(cardNumber, expiration, cvv):

        try:

            today = datetime.now()
            if len(cardNumber == 16) and len(3 <=
                                             cvv <= 4) and expiration > today:

                return True

        except Exception:

            raise


class Order(app.Task):

    def orderInvoice(user, items):

        method = 'orderInvoice'
        template = 'temp'
        res = emailFactory(method, user, items, template)
        send_email()

        return res

    def orderNotification(farmer, user, items):

        method = 'orderNotification'
        template = 'temp'
        res = emailFactory(method, farmer, user, items, template)

        return res

    def orderEnroute(user, items):

        method = 'orderEnroute'
        template = 'temp'
        res = emailFactory(method, user, items, template)

        return res
