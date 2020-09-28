# Import functions and objects the microservice needs.
# - Flask is the top-level application. You implement the application by adding methods to it.
# - Response enables creating well-formed HTTP/REST responses.
# - requests enables accessing the elements of an incoming HTTP/REST request.
#
import json

# Setup and use the simple, common Python logging framework. Send log messages to the console.
# The application should get the log level out of the context. We will change later.
#

import os
import sys
import platform
import socket

import logging
from datetime import datetime

from flask import Flask, Response
from flask import request

from comment_service.service import CommentService

__comment_service = CommentService()

cwd = os.getcwd()
sys.path.append(cwd)
print("*** PYHTHONPATH = " + str(sys.path) + "***")


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Create the application server main class instance and call it 'application'
# Specific the path that identifies the static content and where it is.
application = Flask(__name__,
                    static_url_path='/static',
                    static_folder='WebSite/static')


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.

    application.run("localhost", port=8010)