from ..flask import db

class Connection(db.Model):

    id = db.Column(db.Integer, primary_key=True)
