Hal9000 - Responder
===================
.. image:: https://travis-ci.org/r-worldnews/hal9000-responder.svg?branch=master
   :target: https://travis-ci.org/r-worldnews/hal9000-responder
.. image:: https://coveralls.io/repos/github/r-worldnews/hal9000-responder/badge.svg?branch=master
   :target: https://coveralls.io/github/r-worldnews/hal9000-responder?branch=master
.. image:: https://requires.io/github/r-worldnews/hal9000-responder/requirements.svg?branch=master
   :target: https://requires.io/github/r-worldnews/hal9000-responder/requirements/?branch=master
   :alt: Requirements Status

This is the responder portion of the Hal9000 slackbot for /r/worldnews slack. It uses slackbot's RTM slack client. 

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
