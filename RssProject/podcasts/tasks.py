from celery import Task
from celery import shared_task

import json
from django.conf import settings
from datetime import datetime
from pytz import timezone

import logging
logger = logging.getLogger("elastic_logger")


from .parsers import save_data_to_db


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = 2
    retry_jitter=True



@shared_task(bind=True, base=BaseTaskWithRetry)
def task_rss_parsing(self, link):
    try:
        save_data_to_db(rss_link=link)
    except Exception as e:
        raise self.retry(exc=e, countdown=5)