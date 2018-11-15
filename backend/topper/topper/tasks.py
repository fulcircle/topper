from __future__ import absolute_import
from celery import shared_task
from topper.updater.update import update


@shared_task
def update_stories():
    update()


update_stories()

