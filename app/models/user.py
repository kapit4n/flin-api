import sys
sys.path.append("..")

from app.db import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())

  def __init__(self, name, email):
    self.name = name
    self.email = email

    def __repr__(self):
      return self.name

  def serialize(self):
    return {
      'name': self.name,
      'email': self.email,
      'id': self.id
    }
