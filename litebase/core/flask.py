import os
import sqlite3

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET'] = 'mysecret'

socketio = SocketIO(app)

def serve(*args, **kwargs) -> None:
    """
    Start the Litebase server.

    :param debug: Enable or disable debug mode.
    :type debug: bool

    :param args: Additional arguments passed to the Flask app.
    :type args: tuple

    :param kwargs: Additional keyword arguments passed to the Flask app.
    :type kwargs: dict

    :return: None
    """

    datapath = os.path.join(os.getcwd(), 'data')

    # Checks if the data directory exists
    if not os.path.exists(datapath):
        
        os.makedirs(datapath)

    # Check if the database file exists
    sqlite3.connect(os.path.join(datapath, 'litebase.db'))

    socketio.run(app, *args, **kwargs)