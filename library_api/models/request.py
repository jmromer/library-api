from sqlalchemy.sql import func

from .. import db


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)
    title = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime,
                          nullable=False,
                          server_default=func.now())

    def __repr__(self):
        return 'Request {}>'.format(self.id)
