from src import celery, LOG_LEVEL, LOG_FILE_DISABLE, LOG_PATH
from src.logger import Log
from src.telegram import send_message
from datetime import datetime

logger = Log('tasks')
logger.set_level(LOG_LEVEL)
if not LOG_FILE_DISABLE:
    logger.set_log_path(LOG_PATH)
    logger.set_file_handler()
logger.set_msg_handler()


@celery.task
def print_time():
    msg = f'現在時間: {datetime.now()}'
    logger.info(msg)
    res = {'data': msg}
    return res


@celery.task
def add_num(x, y):
    ans = x + y
    logger.info(ans)
    res = {'data': ans}
    return res
