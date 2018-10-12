import json
from functools import wraps
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from flask import Flask, request
from flask_restplus import Resource, Api
from flask_restplus import fields, abort
from flask_restplus import inputs, reqparse
from itsdangerous import SignatureExpired, JSONWebSignatureSerializer, BadSignature

<<<<<<< HEAD
# Connect to mlab
class Connect(object):
    @staticmethod    
    def get_connection():
        # Waiting for data_cleasing
        return MongoClient("mongodb://<username>:<password>@<correct url>")

# Construct API
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'AUTH-TOKEN'
    }
}

app = Flask(__name__)
api = Api(app,
          default="Install Predict",  # Default namespace
          title="App Dataset",  # Documentation Title
          description="According to basic dataset, predict installs of App", # Documentation Description)
          authorizations=authorizations,
          security='apikey') # Set Authentication Model

predict_model = api.model('App',
                          {'App_name': fields.String},
                          {'category': fields.String},
                          {'rating_of_comparable_app': fields.Float},
                          {'size': fields.Integer},
                          {'price': fields.Float},
                          {'content_rating': fields.Float},
                          {'Android_version': fields.String})

data_type = ['App_name', 'category', 'rating_of_comparable_app', 'size', 'price', 'content_rating', 'Android_version']

credential_parser = reqparse.RequestParser()
credential_parser.add_argument('username', type = str)
credential_parser.add_argument('password', type = str)


# Authentation part
class AuthenticationToken:
    def __init__(self, secret_key, expires_in):
        self.secret_key = secret_key
        self.expires_in = expires_in
        self.serializer = JSONWebSignatureSerializer(secret_key)

    def generate_token(self, username):
        info = {
            'username': username,
            'creation_time': time()
        }

        token = self.serializer.dumps(info)
        return token.decode()

    def validate_token(self, token):
        info = self.serializer.loads(token.encode())

        if time() - info['creation_time'] > self.expires_in:
            raise SignatureExpired("The Token has been expired; get a new token")

        return info['username']


# This means, firstly, customer should be at 'www.abc.com/log_in'
# and then if username and password are correct, should be transfer
# to a new route which is 'www.abc.com/predict'. In this case,
# CLIENT-SIDE should retransmit GIVEN TOKEN and other information
# Specially, GIVEN TOKEN should in a format of HEADER. If this is too
# hard to implement, please tell me and I will change it.
@api.route('/log_in')
class Token(Resource):
    @api.response(200, 'Successful')
    @api.doc(description="Generates a authentication token")
    @api.expect(credential_parser, validate=True)
    def get(self):
        args = credential_parser.parse_args()

        username = args.get('username')
        password = args.get('password')
        
        # This part may be changed due to our idea
        if username == 'admin' and password == 'admin':
            return {'token': auth.generate_token(username)}

        return {'message': 'authorization has been refused for those credentials.'}, 401


# Pretty complex and confusing ('wraps' only).
# Please do not ask me why.
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get('AUTH-TOKEN')
        if not token:
            abort(401, 'Authentication token is missing')

        try:
            user = auth.validate_token(token)
        except SignatureExpired as e:
            abort(401, e.message)
        except BadSignature as e:
            abort(401, e.message)

        return f(*args, **kwargs)

    return decorated


# Request part
@api.route('/predict')
class App_predict(Resource):

    @api.response(200, 'Successful')
    @api.response(400, 'Bad request')
    @api.doc(description="Receive data and give prediction")
    @api.expect(predict_model, validate = True)
    @requires_auth
    def get(self):
        # Justify if there is no data inside
        predict = request.json
        for i in data_type:
            if not predict[i]:
                return {'message': 'Please make sure that you enter all features'}, 400

        # ML model function
        result = ML_function(predict['App_name'], predict['category'], predict['rating_of_comparable_app'], 
                             predict['size'], predict['price'], predict['content_rating'], predict['Android_version'])

        return {'Result': result}


if __name__ == '__main__':
    # Get data from mlab
    connection = Connect.get_connection()
    
    # Authentation Initialization
    SECRET_KEY = "A SECRET KEY, USUALLY A VERY LONG RANDOM STRING. ANYWAY, IT REALLY DOES NOT MATTER WHAT IT IS."
    # Expiring time could be changed
    # In this case, time is setted as 10 mins
    expires_in = 600
    auth = AuthenticationToken(SECRET_KEY, expires_in)
    app.run(debug = True)
=======
>>>>>>> 2832d00c58018bdb1f924ccb834d9975f3d6de6d
