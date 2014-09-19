
.. _Pusher: https://pusher.com/

================================================================================
Chat room sandbox
================================================================================

A proof of concept chat room application on Heroku using Django and the Pusher_
add-on.

Utilizes private channels to propagate changes to users in realtime securely.

Quickstart
================================================================================

First, create an application on Pusher_. Retrieve the ``secret`` and make it
available in the environment via::

    export PUSHER_SECRET=mysecret

Then, to the start the web server in development mode, simply::

    make server

Alternatively, to start the web server in production mode, simply::

    make sever ENV=production

Deploying to Heroku
================================================================================

You will need to define your Pusher secret key via::

    heroku config:set PUSHER_SECRET=mysecret
