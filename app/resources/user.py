from flask_restful import Resource

class UsersAPI(Resource):
  def get(self, id=None):
    if not id:
      return []

    return {'name': 'Luis Arce', 'id': id, 'email': 'luis.arce22@gmail.com'}

  def put(self, id):
    pass

  def delete(self, id):
    pass
