from celery import Celery

app = Celery('topper', broker='redis://redis:6379/0')