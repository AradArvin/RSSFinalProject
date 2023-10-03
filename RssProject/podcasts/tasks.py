from celery import Task
from celery import shared_task
from .parsers import save_data_to_db

import logging
logger = logging.getLogger('celery')



class BaseTaskWithRetry(Task):
    autoretry_for = (Exception,)
    retry_backoff = 2
    retry_jitter=True
    retry_kwargs = {'max_retries': 5}




@shared_task(bind=True, base=BaseTaskWithRetry)
def task_rss_parsing(self, link):
    try:
        save_data_to_db(rss_link=link)
        logger.info('Parsing started...')
    except Exception as e:
        logger.error(e)
        raise Exception(e)