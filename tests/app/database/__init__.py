from app.routes import db


class User(b.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=True)
    activate = db.Column(db.Boolean, nullable=False, default=1)

def __repr__(self):
    return "<User %r>" % self.first_name

