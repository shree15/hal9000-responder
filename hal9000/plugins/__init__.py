""" hal9000 plugin settings """
# pylint: disable=c0103
import praw

from slackbot.settings import REDDIT

reddit = praw.Reddit(client_id=REDDIT['CLIENT_ID'],
                     client_secret=REDDIT['CLIENT_SECRET'],
                     user_agent=REDDIT['USER_AGENT'],
                     username=REDDIT['USER'],
                     password=REDDIT['PASSWORD'])
