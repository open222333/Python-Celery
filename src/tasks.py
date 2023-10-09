from src import celery
from datetime import datetime


@celery.task
def print_time():
    msg = f'現在時間: {datetime.now()}'
    print(msg)
    return msg


@celery.task
def add_num(x, y):
    ans = f'{x} + {y} = {x + y}'
    print(ans)
    return ans
