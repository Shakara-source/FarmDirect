from celery import Celery

app = Celery('tasks', broker='amqp://localhost')


@app.task
def newOrder(payload):

    try:
        twitter = Twitter(oauth)
        twitter.update_status(tweet)
    except (Twitter.FailWhaleError, Twitter.LoginError) as exc:
        
        raise self.retry(exc=exc)

