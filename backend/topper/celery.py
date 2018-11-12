from celery import Celery

app = Celery('topper', broker='redis://localhost/0')