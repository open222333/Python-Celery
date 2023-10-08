from src import celery
from src.schedule import CELERYBEAT_SCHEDULE

celery.conf.update(CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE)

# if __name__ == '__main__':
#     celery.start()
