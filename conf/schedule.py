from datetime import timedelta
from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    'task-name-1': {
        'task': 'src.tasks.print_time',
        'schedule': crontab(hour=12, minute=0),  # 每天中午 12:00 執行
        # 'args': (8, 8)
    },
    'task-name-2': {
        'task': 'src.tasks.print_time',
        'schedule': timedelta(seconds=1),  # 每 30 秒執行一次
        # 'args': (16, 16)
    }
}
