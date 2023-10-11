from celery import Task
from celery import shared_task
import logging

from .parsers import save_data_to_db

logger = logging.getLogger("celery_log")

class BaseTaskWithRetry(Task):
    retry_backoff = 2
    retry_jitter=True



@shared_task(bind=True, base=BaseTaskWithRetry)
def task_rss_parsing(self, link):
    try:
        save_data_to_db(rss_link=link)
    except Exception as e:
        logger.exception(f"Parsing Error: {e}")
        raise self.retry(exc=e, countdown=5)