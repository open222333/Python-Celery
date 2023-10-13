from src import TELEGRAM_API_KEY, TELEGRAM_CHAT_ID, CREATE_CHAT_ID, LOG_FILE_DISABLE, LOG_LEVEL, LOG_PATH
from src.logger import Log
import requests


logger = Log('Telegram')
logger.set_level(LOG_LEVEL)
if not LOG_FILE_DISABLE:
    logger.set_log_path(LOG_PATH)
    logger.set_file_handler()
logger.set_msg_handler()


def send_message(message: str):
    """發送訊息到TG

    Args:
        message (str): 訊息內容
    """
    if TELEGRAM_API_KEY:
        url = f'https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage'
        data = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message
        }
        response = requests.post(url, data=data)
        if response.status_code != 200:
            logger.error(f'無法發送訊息至 Telegram:\n{response.json()}')
            data = {
                'chat_id': CREATE_CHAT_ID,
                'text': f'無法發送訊息至 Telegram:\n{response.json()}'
            }
            requests.post(url, data=data)
