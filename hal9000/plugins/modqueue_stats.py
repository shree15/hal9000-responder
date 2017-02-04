""" Worldnews modqueue stats plugin """
#pylint: disable=C0111
import math
import re
from slackbot.bot import listen_to
from hal9000.plugins import reddit

@listen_to(r'^\.modqueue_stats\s*$', re.I)
@listen_to(r'^\.qstats\s*$', re.I)
def modqueue_status(message):
    message.react('hourglass')

    worldnews = reddit.subreddit('worldnews')
    comments = 0
    submissions = 0

    for _ in worldnews.mod.modqueue(only='comments'):
        comments += 1

    for _ in worldnews.mod.modqueue(only='submissions'):
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


# @listen_to(r'^\.qempty$', re.I)
# def test_q_emtpy(message):
#     message.react('hourglass')
#     message.react('partyparrot')
#     message.reply(':partyparrot: Queue is empty! :partyparrot:')


# @listen_to(r'^\.me\s*$', re.I)
# def get_me(message):
#     message.react('hourglass')
#     message.reply(reddit.user.me().name)


