import sys
# sys.path.append("..")

from app.models.user import User

from flask import jsonify
from flask_restful import Resource, reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('name')
user_parser.add_argument('email')


class UsersAPI(Resource):

  def post(self):
    parsed_user = user_parser.parse_args()
    user = User(parsed_user["name"], parsed_user["email"])
    db.session.add(user)
    db.session.commit()

  def get(self, id=None):
    if not id:
      users = User.query.all()
      return jsonify([u.serialize() for u in users])

    user = User.query.get(id)
    if user:
      return jsonify(user.serialize())
    
    return {"error": "No found user"}

  def put(self, id):
    pass

  def delete(self, id):
    pass
