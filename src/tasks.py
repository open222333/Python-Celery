from src import celery
from datetime import datetime
import pytz

@celery.task
def print_time():
    print(f'現在時間: {datetime.now()}')
