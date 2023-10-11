from src import celery, LOG_LEVEL, LOG_FILE_DISABLE
from src.logger import Log
from datetime import datetime

logger = Log('tasks')
logger.set_level(LOG_LEVEL)
if not LOG_FILE_DISABLE:
    logger.set_file_handler()
logger.set_msg_handler()


@celery.task
def print_time():
    msg = f'現在時間: {datetime.now()}'
    logger.info(msg)
    return msg


@celery.task
def add_num(x, y):
    ans = f'{x} + {y} = {x + y}'
    logger.info(ans)
    return ans
