from configparser import ConfigParser
# from kombu import Exchange, Queue
from celery import Celery
import json
import os


conf = ConfigParser()
conf.read(os.path.join('conf', 'config.ini'))

# celery設定
CELERY_BROKER = conf.get('BASIC', 'CELERY_BROKER', fallback='redis://redis:6379/0')
CELERY_BACKEND = conf.get('BASIC', 'CELERY_BACKEND', fallback='mongodb://mongo:27017/celery.result')
CELERY_TIMEZONE = conf.get('BASIC', 'CELERY_TIMEZONE', fallback='Asia/Taipei')

# log設定
LOG_LEVEL = conf.get('BASIC', 'LOG_LEVEL', fallback='WARNING')

# tasks json設定檔位置
TASKS_JSON_PATH = conf.get('BASIC', 'TASKS_JSON_PATH', fallback=os.path.join('conf', 'tasks.json'))

if os.path.exists(TASKS_JSON_PATH):
    with open(TASKS_JSON_PATH, 'r') as f:
        TASKS = json.loads(f.read())

print(TASKS)

# 指定 MongoDB 作為 backend，這裡使用了 MongoDB 的一個範例 URL
celery = Celery(
    'main',
    broker=CELERY_BROKER,
    backend=CELERY_BACKEND,
    include=['src.tasks'],  # 包含任務定義的模組
)

# CELERY_DEFAULT_QUEUE = 'default'
# CELERY_QUEUES = (
#     Queue('default', Exchange('default'), routing_key='default'),
#     Queue('queue1', Exchange('queue1'), routing_key='queue1'),
#     Queue('queue2', Exchange('queue2'), routing_key='queue2'),
#     # 其他佇列...
# )

# celery 配置
celery.conf.update(
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERY_DEFAULT_QUEUE='default',
    CELERY_REDIRECT_STDOUTS_LEVEL=LOG_LEVEL,
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_SERIALIZER='json',
    CELERY_TIMEZONE=CELERY_TIMEZONE,
    CELERY_TRACK_STARTED=True,
    ENABLE_UTC=True,
)
