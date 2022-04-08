import requests

Api_Key = "deb93c030e3a552f141e93a542f5a587-38029a9d-1eb50df8"
Domain = "https://api.mailgun.net/v3/sandbox70466e0d8d3748df803876b154787cfa.mailgun.org"
FarmDirect_Mail = "no-reply@farmdirect.com"


def send_email(subject, email):
    return requests.post(
        Domain,
        auth=("api", Api_Key),
        data=({"from": FarmDirect_Mail,
              "to": email,
               "subject": subject,
               "text": "{}"})
    )



