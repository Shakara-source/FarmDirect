from Worker import app
from datetime import datetime
from Infrastructure.Services.MailGun import send_email


class Payments(app.Task):

    # Mocks a payment verification service such as stripe

    def verify(cardNumber, expiration, cvv):

        try:

            today = datetime.now()
            if len(cardNumber == 16) and len(3 <= cvv <= 4) and expiration > today:

                return True

        except CardReject:

            raise


class Order(app.Task):

    def shopperReceipt(email, items, orderId):

        subject = "Your FarmDirect order {}".format(orderId)
        text = "Hello, Thank you for your order! {}".format(
            items)
        send_email('orderReceipt', subject, email, text)

    def notifyFarmer(email, items, shopper, address):

        subject = "New Orders from {}".format(shopper)
        text = "Hello, Please send the following: {}".format(
            items) + "to the following address {}".format(address)
        send_email('farmerReceipt', subject, email, text)

    def deliver():

        pass

    def notifyShopper():

        pass
