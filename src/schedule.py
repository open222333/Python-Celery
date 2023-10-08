from datetime import timedelta
from celery.schedules import crontab
from src import TASKS


CELERYBEAT_SCHEDULE = {}

CELERYBEAT_SCHEDULE['test'] = {
    'task': 'src.tasks.print_time',
    'schedule': timedelta(seconds=1),  # 每 1 秒執行一次
}

task_name = 'print_time-1'
if task_name in TASKS.keys():
    if TASKS[task_name]['execute']:
        if TASKS[task_name]['queue']:
            queue = TASKS[task_name]['queue']
        else:
            queue = 'queue1'

        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'src.tasks.print_time',
            'schedule': timedelta(seconds=1),  # 每 1 秒執行一次
            'options': {'queue': queue}  # 將任務發送到 queue
        }

task_name = 'print_time-2'
if task_name in TASKS.keys():
    if TASKS[task_name]['execute']:
        if TASKS[task_name]['queue']:
            queue = TASKS[task_name]['queue']
        else:
            queue = 'queue1'

        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'src.tasks.print_time',
            'schedule': crontab(hour=12, minute=0),  # 每天中午 12:00 執行
            'options': {'queue': queue}  # 將任務發送到 queue
        }

task_name = 'add_num-1'
if task_name in TASKS.keys():
    if TASKS[task_name]['execute']:
        if TASKS[task_name]['queue']:
            queue = TASKS[task_name]['queue']
        else:
            queue = 'queue1'

        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'src.tasks.add_num',
            'schedule': timedelta(seconds=1),  # 每 1 秒執行一次
            'args': tuple(TASKS[task_name]['args']),  # 帶入參數 將串列轉成元組
            'options': {'queue': queue}  # 將任務發送到 queue
        }
