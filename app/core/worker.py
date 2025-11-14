import os
from celery import Celery
from celery.utils.log import get_task_logger
from app.core.config import config

app = Celery(
    'worker',
    broker=config.CELERY_BROKER_URL,
    # backend=config.CELERY_RESULT_BACKEND
)
logger = get_task_logger(__name__)


@app.task
def add(x, y):
    logger.info(f'Adding {x} + {y}')
    return x + y