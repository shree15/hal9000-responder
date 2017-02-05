Worldnews SlackBot
==================

This bot has two parts, an message responder and a periodic scheduler. The responder is based on slackbot using a custom bot integration, while the periodic routine is based on schedule and uses as webhook.  This is largely because slackbot does not have any mechanisms for periodic routines like scanning modmail.

.. _Installation:

Installation
------------

Download from git:

.. code-block:: bash

    git clone https://github.com/r-worldnews/hal9000-responder.git

Create config file from example:

.. code-block:: bash

    cp slackbot_settings.py.example slackbot_settings.py

On slack create a custom bot integration and set `API_TOKEN` in `slackbot_settings.py`.

Create a script application on reddt and set the credentials in `REDDIT`

Install the requirements:

.. code-block:: bash

    pip install -r requirements.txt

Start the bot:

.. code-block:: bash

    python run.py
    
.. _License:

License
-------

This is released under the MIT license.
