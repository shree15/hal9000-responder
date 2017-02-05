""" hal9000 plugin settings """
# pylint: disable=c0103
import praw

from slackbot_settings import REDDIT
from hal9000 import __version__

USER_AGENT = "linux:{}:hal9000-responder by /u/praisebetoscience"
reddit = praw.Reddit(client_id=REDDIT['CLIENT_ID'],
                     client_secret=REDDIT['CLIENT_SECRET'],
                     user_agent=USER_AGENT.format(__version__),
                     username=REDDIT['USER'],
                     password=REDDIT['PASSWORD'])
