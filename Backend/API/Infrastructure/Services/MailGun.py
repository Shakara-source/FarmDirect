import requests
from fastapi.responses import JSONResponse

Api_Key = "deb93c030e3a552f141e93a542f5a587-38029a9d-1eb50df8"
Domain = "https://api.mailgun.net/v3/sandbox70466e0d8d3748df803876b154787cfa.mailgun.org"
FarmDirect_Mail = "no-reply@farmdirect.com"


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

        Emails.orderInvoice(args)

    elif emailType == 'orderNotification':

        Emails.orderNotification(args)

    elif emailType == 'orderEnroute':

        Emails.orderEnroute(args)


class Emails:

    def orderInvoice(user, items, template):

        try:
            to = user.email
            subject = 'FarmDirect Order Confirmation'
            temp = template
            text = "Hello {name}, Your order was recieved for the following items: {items}. Thank you for shopping with FarmDirect!".format(
                name=user.name, items=items)

            send_email(to, subject, temp, text)

            return JSONResponse(content={"description": "Message sent"},
                                status_code=200)

        except Exception:

            return JSONResponse(content={"description": "Failed to send"},
                                status_code=400)

    def orderNotification(farmer, items, user, template):

        try:
            to = farmer.email
            subject = 'New FarmDirect Order'
            temp = template
            text = "Hello {name}, an order was recieved for the following items: {items}. Please send the following to the following address {shippingaddress}. Thanks, FarmDirect Team ".format(
                name=farmer.name, items=items, shippingaddress=user.shippingaddress)

            send_email(to, subject, temp, text)

            return JSONResponse(content={"description": "Message sent"},
                                status_code=200)

        except Exception:

            return JSONResponse(content={"description": "Failed to send"},
                                status_code=400)

    def orderEnroute(user, items, template):

        try:
            to = user.email
            subject = 'FarmDirect Order Shipped!'
            temp = template
            text = "Hello {name}, the following items were shipped: {items}. Thanks, FarmDirect Team ".format(
                name=user.name, items=items)

            send_email(to, subject, temp, text)

            return JSONResponse(content={"description": "Message sent"},
                                status_code=200)

        except Exception:

            return JSONResponse(content={"description": "Failed to send"},
                                status_code=400)
