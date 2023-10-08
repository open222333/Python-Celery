from src import celery
from datetime import datetime


@celery.task
def print_time():
    print(f'現在時間: {datetime.now()}')


@celery.task
def add_num(x, y):
    print(f'{x} + {y} = {x + y}')
