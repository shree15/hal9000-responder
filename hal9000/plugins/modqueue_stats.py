""" Worldnews modqueue stats plugin """
# pylint: disable=C0111
import logging
import math
import re
from slackbot.bot import listen_to
from hal9000.plugins import reddit

logger = logging.getLogger(__name__)

@listen_to(r'^\.modqueue_stats\s*$', re.I)
@listen_to(r'^\.qstats\s*$', re.I)
def modqueue_stats(message):
    message.react('hourglass')

    logger.debug('Modqueue stats body: %s', message.body)
    logger.info('Moqueue stats request from: %s', 'test')

    worldnews = reddit.subreddit('worldnews')
    comments = 0
    submissions = 0

    for thing in worldnews.mod.modqueue(limit=2000):
        if thing.name.startswith('t1'):
            comments += 1
        if thing.name.startswith('t3'):
            submissions += 1

    total = comments + submissions
    pages = math.ceil(total / 25)

    if total:
        reply = "Modqueue currently contains {} items ({} comments, " \
                "{} submissions) spanning {} pages."

        message.reply(reply.format(total, comments, submissions, pages))

    else:
        message.react('partyparrot')
        message.reply(':partyparrot: Queue is empty! :partyparrot:')
