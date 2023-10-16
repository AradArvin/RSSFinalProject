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

    def on_retry(self, exc, task_id, args, kwargs, einfo):

        log_data = {
            "task_id":task_id,
            "exe":str(exc),
            "event":f"Celery task >>> {self.name}",
            "args":args,
            "kwargs":kwargs,
            "happend_on":datetime.now(timezone(settings.TIME_ZONE)),
            "status":"retry"
        }
        logger.exception(json.dumps(log_data))
        return super().on_retry(exc, task_id, args, kwargs, einfo)
    



@shared_task(bind=True, base=BaseTaskWithRetry)
def task_rss_parsing(self, link):
    try:
        save_data_to_db(rss_link=link)
    except Exception as e:
        raise self.retry(exc=e, countdown=5)