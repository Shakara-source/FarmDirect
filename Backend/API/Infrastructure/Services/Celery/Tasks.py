from Worker import app 
import time

class AuthenticatePayment(app.Task):

    def __init__(self,cardNumber):
        self.number = 

    def status(self):
        if 
        time.sleep(15)
        return True



class NewOrder(app.Task):

    def __init__(self,orderId,farmerId,shopperId):
        self.orderId = orderId
        self.shopperId = shopperId
        self.farmerId = farmerId 

    def postageLabel(self):

        return label
    
    def emailFarmer(self):

        subject = "Farm Direct Order number {}".format(self.orderId)
        message = "Hello {}, Your shipment ".format(self.)

    def emailShopper(self):

        subject = "Farm Direct Order number {}".format(self.orderId)
        message = "Hello {}, A customer ordered the following items:{}".format()

class DeliverOrder(app.Task):

    def __init__(self,orderId, shopperId):
        self.orderId = orderId,
        self.shopperId = shopperId

    def emailShopper(self):

        subject = "Farm Direct Order number {}".format(self.orderId)
        message = "Hello {}, A customer ordered the following items:{}".format()
    
    def commitDelivery(self):

        time.sleep(3600)


@app.task
def newOrder(payload):

    try:
        twitter = Twitter(oauth)
        twitter.update_status(tweet)
    except (Twitter.FailWhaleError, Twitter.LoginError) as exc:
        
        raise self.retry(exc=exc)

