#!/bin/bash
#
#    curl example
#    ~~~~~~~~~~~~
#
#    This provides an example of using Flask-Restless on the server-side to
#    provide a ReSTful API and `curl <http://curl.haxx.se/>`_ on the client
#    side to make HTTP requests to the server.
#
#    In order to use this script, you must first run the quickstart server
#    example from this directory:
#
#        PYTHONPATH=.. python quickstart.py
#
#    Now run this script from this directory (that is, the ``examples/``
#    directory) see some example requests made from curl.
#
#    The important thing to note in this example is that the client must
#    remember to specify the ``application/json`` MIME type when sending
#    requests.
#
#    :copyright: 2012 Jeffrey Finkelstein <jeffrey.finkelstein@gmail.com>
#    :license: GNU AGPLv3+ or BSD

# We expect the server to be running at 127.0.0.1:5000, the Flask default.
HOST=127.0.0.1:5000

echo
echo "Making an initial GET request..."
echo
# curl makes GET requests by default.
curl -H "Content-type: application/json" http://$HOST/api/user

echo
echo
echo "Making a POST request..."
echo
curl -X POST -H "Content-type: application/json" http://$HOST/api/user \
    -d '{"username": "jdot", "email": "jdot@jdot.com"}'

curl -X POST -H "Content-type: application/json" http://$HOST/api/user \
    -d '{"username": "mike", "email": "mike@mike.com"}'
curl -X POST -H "Content-type: application/json" http://$HOST/api/user \
    -d '{"username": "jason", "email": "jason@jason.com"}'
echo
echo
echo "Making a GET request for the entire collection..."
echo
curl -H "Content-type: application/json" http://$HOST/api/user

echo
echo
echo "Making a GET request for the added person..."
echo
curl -H "Content-type: application/json" http://$HOST/api/user/1
echo
