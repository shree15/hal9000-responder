# notifies slack of a new modmail sent to worldnews from user.
import logging
import time

from .slack_webhook import SlackWebhook as sb

MAX_AGE = 60 * 60 * 5
IGNORE_USERS = ['automoderator', 'worldnewsmods']
MESSAGE_URL = "https://reddit.com/message/messages/{}"
# NEW_MODMAIL_MESSAGE = """New Modmail!
# Author: <https://reddit.com/u/{author}|{author}>
# Subject: <{link}|{subject}>
# """

NEW_MODMAIL_MESSAGE = 'New Modmail: ' \
    '[<https://reddit.com/u/{author}|{author}>] ' \
    '<{link}|{subject}>'

logger = logging.getLogger(__name__)


def modmail_handler(reddit, db):
    """Retrieve inbox and route messages to individual alerts"""
    worldnews = reddit.subreddit('worldnews')
    for msg in worldnews.mod.inbox(limit=20):
        if is_read(db, msg.name):
            continue

        # dispatchers
        new_modmail(msg)
        many_reports(msg)

        mark_read(db, msg.name)


def new_modmail(msg):
    """Send alert on new message from user"""
    age = get_age(msg.created_utc)

    if age > MAX_AGE:
        return
    if msg.author.lower() in IGNORE_USERS:
        return
    if msg.replies:
        return

    link = get_modmail_link(msg)

    logger.info("New Modmail: %s, %s, %s", msg.author, msg.subject, link)

    sb.send(NEW_MODMAIL_MESSAGE.format(author=msg.author,
                                       subject=msg.subject,
                                       link=link),
            channel='modupdates')


def many_reports(msg):
    if msg.author.lower() != "automoderator":
        return
    if "has many reports, please review." not in msg.subject:
        return

    link = get_modmail_link(msg)

    logger('High Reports: %s', link)

    sb.send("<{}|Submission with 4+ reports>".format(link))


def get_age(created_utc):
    current_time = int(time.time())
    return int(current_time - created_utc)


def get_modmail_link(msg):
    msg_id = msg.name.split('_')[1]
    return MESSAGE_URL.format(msg_id)


def is_read(db, id):
    return db['read_modmail'].find_one(name=id)


def mark_read(db, id):
    db.begin()
    try:
        db['read_modmail'].insert(dict(name=id, utc=int(time.time())))
        db.commit()
    except:
        db.rollback()
