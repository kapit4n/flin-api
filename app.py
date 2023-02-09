from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os


import app.resources.user as userResources

from app.models.user import User, db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)
db.create_all()

api = Api(app)

api.add_resource(userResources.UsersAPI, '/users/', '/users/<id>')

if __name__ == '__main__':
  app.run(debug=True)
