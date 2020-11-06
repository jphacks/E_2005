from bot import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Text)
    raspi_id = db.Column(db.Text)
    user_name = db.Column(db.Text)

    def __repr__(self):
        return "<line_id={self.line_id} raspi_id={self.raspi_id} user_name={self.user_name}>".format(self=self)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Text)
    line_status = db.Column(db.Integer)

    def __repr__(self):
        return "<line_id={self.line_id} line_status={self.line_status}>".format(self=self)

class Whole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text)
    tag = db.Column(db.Text)

    def __repr__(self):
        return "<word={self.word} tag={self.tag}>".format(self=self)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text)
    tag = db.Column(db.Text)
    raspi_id = db.Column(db.Text)

    def __repr__(self):
        return "<word={self.word} tag={self.tag} raspi_id={self.raspi_id}>".format(self=self)
class Call(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    raspi_id = db.Column(db.Text)
    text = db.Column(db.Text)
    key = db.Column(db.Text)

    def __repr__(self):
        return "<raspi_id={self.raspi_id}, text={self.text} key={self.key}>".format(self=self)

def init():
    db.create_all()
