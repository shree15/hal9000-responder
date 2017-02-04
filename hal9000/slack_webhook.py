import logging
import requests
from hal9000 import WEBHOOK

logger = logging.getLogger(__name__)


class SlackWebhook(object):

    WEBHOOK = WEBHOOK

    @classmethod
    def send(cls,
             msg, channel='bot_testing', username='hal9000', icon_emoji=''):
        payload = {
            'text': msg,
            'channel': "#" + channel,
            'username': username,
            'icon_emoji': icon_emoji
        }

        logger.debug('Sending msg: %s', str(payload))
        requests.post(cls.WEBHOOK, json=payload)
