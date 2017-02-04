import logging
from time import sleep

import dataset
import praw
import requests
import schedule

from slackbot_settings import REDDIT, WEBHOOK, VERSION
from .modmail_notification import modmail_handler


USER_AGENT = "linux:{}:hal9000 slackbot periodic by /u/praisebetoscience"
reddit = praw.Reddit(client_id=REDDIT['CLIENT_ID'],
                     client_secret=REDDIT['CLIENT_SECRET'],
                     user_agent=USER_AGENT.format(VERSION),
                     username=REDDIT['USER'],
                     password=REDDIT['PASSWORD'])

db = dataset.connect('sqlite:///sql.db')

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
TIMEFMT = '%Y-%m-%d %H:%M%S %z]'
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s',
                              datefmt=TIMEFMT)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


def run():
    schedule.every(1).minute.do(modmail_handler, reddit, db)

    while True:
        try:
            schedule.run_pending()
            sleep(1)
        except KeyboardInterrupt:
            db.commit()
            exit()
        except Exception as err:
            logging.error(err)
            sleep(10)
