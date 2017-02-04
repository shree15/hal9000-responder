# Worldnews SlackBot

This bot has two parts, an message responder and a periodic scheduler. The responder is based on slackbot using a custom bot integration, while the periodic routine is based on schedule and uses as webhook.  This is largely because slackbot does not have any mechanisms for periodic routines like scanning modmail.

## Installation.

Download from git:

    git clone https://

Create config file from example:

    cp slackbot_settings.py.example slackbot_settings.py 

On slack create a custom bot integration and set `API_TOKEN` in `slackbot_settings.py`.

Create a Webhook in slack and set `WEBHOOK` to the url generated.

Create a script applicatio on reddt and set the credentials in `REDDIT`

For the responder run `run_slackbot.py`.  For the periodic bot run `run_periodic.py`.  

## License

This is released under the MIT license. 
