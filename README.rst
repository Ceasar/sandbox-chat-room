================================================================================
Chat room sandbox
================================================================================

A proof of concept chat room application on Heroku using Django and the Pusher
add-on.

Utilizes private channels to propagate changes to users in realtime securely.

Quickstart
================================================================================

To the start the web server in development mode, simply::

    make server

To start the web server in production mode::

    make sever ENV=production

Deploying to Heroku
================================================================================

You will need to define your Pusher secret key via::

    heroku config:set PUSHER_SECRET=mysecret
