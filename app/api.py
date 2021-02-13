import json
from functools import wraps
import datetime
import jwt
import requests
from flasgger import Swagger
from flask import request, jsonify
from app import app
from app.input_schema import TrainingAPISchema, LoginInputSchema

swagger = Swagger(app, template=app.config['SWAGGER_TEMPLATE'])


@app.route('/login', methods=['POST'])
def login():

    return 0
