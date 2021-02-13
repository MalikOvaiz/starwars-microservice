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


@app.route('/starships', methods=['POST'])
def starships():
    """Endpoint for training dss system for munitions
    This is using docstrings for specifications.
    ---
    parameters:
      - name: sort
        in: formData
        type: integer
        enum: [0,1,2]
        required: true
        default: 0
        description: Microservice to return starships from the Star Wars movies, sorted by the hyperdrive rating. 0 without sort, 1 sort Asc, 2, sort Desc
    responses:
      200:
        description: JSON object containing starships
        examples:
          rgb: []
    """
    return 0
