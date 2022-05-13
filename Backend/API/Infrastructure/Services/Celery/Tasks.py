from Worker import app
from Application.Models.OrderDTO import CardSchema
from celery.utils.log import get_task_logger
from Infrastructure.Services.MailGun import emailFactory
from Infrastructure.Services.Card import CardServices

celery_log = get_task_logger(__name__)


@app.task(name='payment.verify')
def verifyCard(data: CardSchema):
    CardServices.verify(data)
    celery_log.info("Celery task completed!")
    return 'Status'


@app.task(name='mailers.send')
def sendEmail(type: str, data):
    emailFactory(type, data)
    celery_log.info("Celery task completed!")
    return 'Status'
