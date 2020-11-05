from bot import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text)
    raspi_id = db.Column(db.Text)

    def __repr__(self):
        return "<user_id={self.user_id} raspi_id={self.raspi_id}>".format(self=self)

def init():
    db.create_all()

