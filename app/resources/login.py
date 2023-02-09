from app.models.user import User
from flask_restful import Resource, reqparse

from datetime import date, timedelta, datetime
import jwt

login_parser = reqparse.RequestParser()
login_parser.add_argument('password')
login_parser.add_argument('email')

class LoginAPI(Resource):
  def post(self):
    parsed_login = login_parser.parse_args()
    user = User.query.filter_by(email=parsed_login["email"]).first()

    if not user:
      return {"error": "Username or password is incorrect"}

    print(jwt.__file__)
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    print('encoded_jwt')
    print(encoded_jwt)

    jwt_token = self.encode_auth_token("llll")
    print(jwt_token)

    decoded_token = jwt_token.decode('UTF-8')

    return {"jwt": decoded_token , "message": "Successfully loged"}

  def encode_auth_token(self, user_id):
    try:
      payload = {
        "exp": datetime.utcnow() + timedelta(days=0, seconds=5),
        'iat': datetime.utcnow(),
        'sub': 'user_id'
      }

      print("LLLLLLLLLLLLLLL")

      jwt_token = jwt.encode(
        payload,
        'SECRETKEY1',
        algorithm="HS256"
      )

      print(jwt_token)

      return jwt_token
    except Exception as e:
      return e



