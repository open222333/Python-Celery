from datetime import timedelta
from celery.schedules import crontab
from src import TASKS


CELERYBEAT_SCHEDULE = {}

task_name = 'print_time-1'
if task_name in TASKS.keys():
    if TASKS[task_name]['execute']:
        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'src.tasks.print_time',
            'schedule': timedelta(seconds=5)  # 每 1 秒執行一次
        }

        if TASKS[task_name]['queue']:
            # 將任務發送到 queue
            CELERYBEAT_SCHEDULE[task_name]['options'] = {'queue': TASKS[task_name]['queue']}

task_name = 'add_num-1'
if task_name in TASKS.keys():
    if TASKS[task_name]['execute']:
        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'src.tasks.add_num',
            'schedule': crontab(hour=12, minute=0),  # 每天中午 12:00 執行
            'args': tuple(TASKS[task_name]['args'])  # 帶入參數 將串列轉成元組
        }

        if TASKS[task_name]['queue']:
            # 將任務發送到 queue
            CELERYBEAT_SCHEDULE[task_name]['options'] = {'queue': TASKS[task_name]['queue']}
