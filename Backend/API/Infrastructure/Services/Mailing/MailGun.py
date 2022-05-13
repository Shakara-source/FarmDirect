import requests
from Backend.API.Application.Models.OrderDTO import OrderInvoiceSchema, FarmerOrderNotificationSchema
from celery.utils.log import get_task_logger

Api_Key = "deb93c030e3a552f141e93a542f5a587-38029a9d-1eb50df8"
Domain = "https://api.mailgun.net/v3/sandbox70466e0d8d3748df803876b154787cfa.mailgun.org"
FarmDirect_Mail = "no-reply@farmdirect.com"

celery_log = get_task_logger(__name__)


def send_email(email, subject, template, text):
    return requests.post(
        Domain,
        auth=("api", Api_Key),
        data=({"from": FarmDirect_Mail,
              "to": email,
               "subject": subject,
               "template": template,
               "text": text})
    )


def emailFactory(emailType, *args):

    if emailType == 'orderInvoice':

        EmailService.orderInvoice(args)

    elif emailType == 'orderNotification':

        EmailService.orderNotification(args)

    elif emailType == 'orderEnroute':

        EmailService.orderEnroute(args)


class EmailService:

    def orderInvoice(data: OrderInvoiceSchema):

        try:
            to = data.shopperEmail
            subject = 'FarmDirect Order Confirmation'
            temp = data.template
            text = "Hello {name}, Your order was recieved for the following items: {items}. Total: ${price} Thank you for shopping with FarmDirect!".format(
                name=data.shopperName, items=data.items, price=data.price)

            send_email(to, subject, temp, text)

            celery_log.info('Sent')

        except Exception:

            celery_log.exception('Send Fail')

    def orderNotification(data: FarmerOrderNotificationSchema):

        try:
            to = data.farmerEmail
            subject = 'New FarmDirect Order'
            temp = data.template
            text = "Hello {name}, an order was recieved for the following items: {items}. Please send the following to the following address {shippingaddress}. Thanks, FarmDirect Team ".format(
                name=data.farmerName,
                items=data.items, shippingaddress=data.orderAddress)

            send_email(to, subject, temp, text)

            celery_log.info('Sent')

        except Exception:

            celery_log.exception('Send Fail')

    def orderEnroute(data: OrderInvoiceSchema):

        try:
            to = data.email
            subject = 'FarmDirect Order Shipped!'
            temp = data.template
            text = "Hello {name}, the following items were shipped: {items}. Thanks, FarmDirect Team ".format(
                name=data.shopperName, items=data.items)

            send_email(to, subject, temp, text)

            celery_log.info('Sent')

        except Exception:

            celery_log.exception('Send Fail')
