import json
from functools import wraps
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from flask import Flask, request
from flask_restplus import Resource, Api
from flask_restplus import fields, abort
from flask_restplus import inputs

# Connect to mlab
class Connect(object):
    @staticmethod    
    def get_connection():
        # Waiting for data_cleasing
        return MongoClient("mongodb://<username>:<password>@<correct url>")

# Construct
app = Flask(__name__)
api = Api(app,
          default="Install Predict",  # Default namespace
          title="App Dataset",  # Documentation Title
          description="According to basic dataset, predict installs of App") # Documentation Description)


predict_model = api.model('App',
                          {'App_name': fields.String},
                          {'category': fields.String},
                          {'rating_of_comparable_app': fields.Float},
                          {'size': fields.Integer},
                          {'price': fields.Float},
                          {'content_rating': fields.Float},
                          {'Android_version': fields.String})

data_type = ['App_name', 'category', 'rating_of_comparable_app', 'size', 'price', 'content_rating', 'Android_version']

@api.route('/predict')
class App_predict(Resource):

    @api.response(200, 'Successful')
    @api.response(400, 'Bad request')
    @api.doc(description="Receive data and give prediction")
    @api.expect(predict_model, validate = True)
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
    app.run(debug = True)
