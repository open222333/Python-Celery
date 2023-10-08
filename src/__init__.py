from configparser import ConfigParser
from celery import Celery
import os


conf = ConfigParser()
conf.read(os.path.join('conf', 'config.ini'))

CELERY_BROKER = conf.get('BASIC', 'CELERY_BROKER', fallback='redis://redis:6379/0')
CELERY_BACKEND = conf.get('BASIC', 'CELERY_BACKEND', fallback='mongodb://mongo:27017/celery.result')
CELERY_TIMEZONE = conf.get('BASIC', 'CELERY_TIMEZONE', fallback='Asia/Taipei')

LOG_LEVEL = conf.get('BASIC', 'LOG_LEVEL', fallback='WARNING')

# 指定 MongoDB 作為 backend，這裡使用了 MongoDB 的一個範例 URL
celery = Celery(
    'main',
    broker=CELERY_BROKER,
    backend=CELERY_BACKEND,
    include=['src.tasks'],  # 包含任務定義的模組
)

# 配置
celery.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TRACK_STARTED=True,
    CELERY_DISABLE_RATE_LIMITS=True,
    ENABLE_UTC=True,
    CELERY_TIMEZONE=CELERY_TIMEZONE,
    CELERY_REDIRECT_STDOUTS_LEVEL=LOG_LEVEL
)
