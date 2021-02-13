import json
from functools import wraps
import datetime
import jwt
import requests
from flasgger import Swagger
from flask import request, jsonify
from app import app
from app.request_validator import StarshipAPISchema
from http import HTTPStatus
from app.repositories.starship import Starship

swagger = Swagger(app, template=app.config['SWAGGER_TEMPLATE'])


@app.route('/starships', methods=['POST'])
def starships():
    """Endpoint for training dss system for munitions
    This is using docstrings for specifications.
    ---
    parameters:
      - name: sort_id
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

    try:
        errors = StarshipAPISchema().validate(request.form)
        if errors:
            message = {
                'status': HTTPStatus.BAD_REQUEST,
                'message': str(errors),
            }
            resp = jsonify(message)
            resp.status_code = HTTPStatus.BAD_REQUEST
            return resp
        sort_id = int(request.form.get('sort_id'))
        data = Starship().get_starships(sort_id)
        return jsonify({
            'status': HTTPStatus.OK,
            'results': data,
        })
    except Exception as e:
        resp = jsonify({
            'message': str(e)
        })
        resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return resp
