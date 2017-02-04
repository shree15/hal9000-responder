import re
from slackbot.bot import listen_to

@listen_to(r'\bonions?\b', re.I)
def react_onion(message):
    message.react('heart')
    message.react('onion')
