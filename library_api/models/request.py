from .. import db


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Additional fields

    def __repr__(self):
        return 'Request {}>'.format(self.id)
