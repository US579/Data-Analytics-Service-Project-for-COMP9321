import json
from functools import wraps
from time import *
import pandas as pd
import numpy as np
import pymongo
import simplejson
from pymongo import MongoClient
from flask import Flask, request
from flask_restplus import Resource, Api
from flask_restplus import fields, abort
from flask_restplus import inputs, reqparse
from flask import make_response
from flask_json import FlaskJSON, as_json_p
from itsdangerous import SignatureExpired, JSONWebSignatureSerializer, BadSignature
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
import pickle
from flask import jsonify
from flask_cors import *

<<<<<<< HEAD

def prediction(category, rating, reviews, size, price, content_rating, android_ver, save_file='trained_model.sav'):
    knn_load = pickle.load(open(save_file, 'rb'))
    pred = knn_load.predict([[category, rating, reviews, size, price, content_rating, android_ver]])
    return pred


=======
def prediction(category, rating, reviews, size, price, content_rating, android_ver, save_file = 'trained_model.sav'):
    knn_load = pickle.load(open(save_file, 'rb'))
    pred = knn_load.predict([[category, rating, reviews, size, price, content_rating, android_ver]])
    return pred
>>>>>>> 81eba1ba8fbf9d84d5ea5d3986ebb3bfbf002fb0
# Construct API
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'AUTH-TOKEN'
    }
}

app = Flask(__name__)
CORS(app)
##json = FlaskJSON(app)
api = Api(app,
          default="Install Predict",  # Default namespace
          title="App Dataset",  # Documentation Title
          description="According to basic dataset, predict installs of App",  # Documentation Description)
          authorizations=authorizations,
          security='apikey')  # Set Authentication Model

predict_model = reqparse.RequestParser()
<<<<<<< HEAD
predict_model.add_argument('reviews', type=float)
predict_model.add_argument('category', type=float)
predict_model.add_argument('rating_of_comparable_app', type=float)
predict_model.add_argument('size', type=float)
predict_model.add_argument('price', type=float)
predict_model.add_argument('content_rating', type=float)
predict_model.add_argument('Android_version', type=float)
=======
predict_model.add_argument('reviews', type = float)
predict_model.add_argument('category', type = float)
predict_model.add_argument('rating_of_comparable_app', type = float)
predict_model.add_argument('size', type = float)
predict_model.add_argument('price', type = float)
predict_model.add_argument('content_rating', type = float)
predict_model.add_argument('Android_version', type = float)
>>>>>>> 81eba1ba8fbf9d84d5ea5d3986ebb3bfbf002fb0

credential_parser = reqparse.RequestParser()
credential_parser.add_argument('username', type=str)
credential_parser.add_argument('password', type=str)


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
@api.route('/login')
class Token(Resource):
    @api.response(200, 'Successful')
    @api.doc(description="Generates a authentication token")
    @api.expect(credential_parser, validate=True)
<<<<<<< HEAD
    # @as_json_p
=======
    #@as_json_p
>>>>>>> 81eba1ba8fbf9d84d5ea5d3986ebb3bfbf002fb0
    def get(self):
        args = credential_parser.parse_args()

        username = args.get('username')
        password = args.get('password')
<<<<<<< HEAD
        data = {"message": auth.generate_token(username)}
        response = jsonify(data)
        response.status_code = 200
        # data = simplejson.dumps(data)
        if username == 'admin' and password == 'admin':
            return response
=======
        data = {"token":auth.generate_token(username)}
        response = jsonify(data)
        response.status_code = 200
        #data = simplejson.dumps(data)
        if username == 'admin' and password == 'admin':
            return  response
>>>>>>> 81eba1ba8fbf9d84d5ea5d3986ebb3bfbf002fb0

        return simplejson.dumps({'message': 'authorization has been refused for those credentials.'}), 401


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
    @api.expect(predict_model, validate=True)
    @requires_auth
    @as_json_p
    def get(self):
        # Justify if there is no data inside
        args = predict_model.parse_args()
        reviews = args.get('reviews')
        category = args.get('category')
        rating_of_comparable_app = args.get('rating_of_comparable_app')
        size = args.get('size')
        price = args.get('price')
        content_rating = args.get('content_rating')
        Android_version = args.get('Android_version')
        print(reviews, category, rating_of_comparable_app,
              size, price, content_rating, Android_version)
<<<<<<< HEAD
        if reviews and category and rating_of_comparable_app and \
                size and content_rating and Android_version:
            ## ML model function
            ## You should return an ensured value if you want to debug

            result = prediction(category, rating_of_comparable_app, reviews, size, price, content_rating,
                                Android_version)
=======
        if reviews and category and rating_of_comparable_app and\
           size and content_rating and Android_version:
            ## ML model function
            ## You should return an ensured value if you want to debug
            
            result = prediction(category, rating_of_comparable_app, reviews, size, price, content_rating, Android_version)
>>>>>>> 81eba1ba8fbf9d84d5ea5d3986ebb3bfbf002fb0
            result = str(result)
            print(result)
            final_result = {'result': result}
            final_result = simplejson.dumps(final_result)

            return final_result, 200
        else:
            return simplejson.dumps({'message': 'Please make sure that you enter all features'}), 400


if __name__ == '__main__':
    # Authentation Initialization
    SECRET_KEY = "A SECRET KEY, USUALLY A VERY LONG RANDOM STRING. ANYWAY, IT REALLY DOES NOT MATTER WHAT IT IS."
    # Expiring time could be changed
    # In this case, time is setted as 100 mins
    expires_in = 6000
    auth = AuthenticationToken(SECRET_KEY, expires_in)
    app.run(debug=True)