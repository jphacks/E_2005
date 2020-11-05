from bot import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text)
    raspi_id = db.Column(db.Text)
    raspi_name = db.Column(db.Text)

    def __repr__(self):
        return "<user_id={self.user_id} raspi_id={self.raspi_id} raspi_name={self.raspi_name}>".format(self=self)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text)
    user_status = db.Column(db.Integer)

    def __repr__(self):
        return "<user_id={self.user_id} user_status={self.user_status}>".format(self=self)

def init():
    db.create_all()