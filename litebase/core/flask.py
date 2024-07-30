import os
import sqlite3

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/data/litebase.db"
app.config['SECRET'] = 'mysecret'

db.init_app(app)
socketio = SocketIO(app)

def serve(debug=False, *args, **kwargs) -> None:
    """
    Start the Litebase server.

    :param debug: Enable or disable debug mode.
    :type debug: bool, default False

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

    # Create the tables
    with app.app_context():

        db.create_all()

    socketio.run(app, debug=debug, *args, **kwargs)
