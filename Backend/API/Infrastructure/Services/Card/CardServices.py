from datetime import datetime
from Application.Models.OrderDTO import CardSchema
from celery.utils.log import get_task_logger

celery_log = get_task_logger(__name__)


class CardServices:

    def verify(data: CardSchema):

        today = datetime.now()
        
        if len(data.cardNumber != 16):
            
            celery_log.exception('Card Date error')
            
        elif len(data.cvv != 3):

            celery_log.exception('Card CVV error')

        elif data.expiration < today:

            celery_log.exception('Card Expiration error')
        
        celery_log.info('Accepted')
