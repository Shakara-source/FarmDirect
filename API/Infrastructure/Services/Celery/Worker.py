from celery import Celery

BROKER_URI = 'amqp://rabbitmq'


app = Celery(
    'celery_tasks',
    broker=BROKER_URI,
    include=['celery_tasks.tasks']
)