from flask import Flask
from flask_restful import Resource, Api

import app.resources.user as userResources

app = Flask(__name__)
api = Api(app)

api.add_resource(userResources.UsersAPI, '/users/', '/users/<id>')

if __name__ == '__main__':
  app.run(debug=True)