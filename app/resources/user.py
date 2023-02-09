import sys
sys.path.append("..")

from app.models.user import User

from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy()

class UsersAPI(Resource):

  def post(self):
    u = User('Luis Arce2', 'luis.222@gmail.com')
    db.session.add(u)
    db.session.commit()


  def get(self, id=None):
    if not id:
      users = User.query.all()
      return jsonify([u.serialize() for u in users])

    return User('Luis Arce', 'get@gmail.com')

  def put(self, id):
    pass

  def delete(self, id):
    pass
