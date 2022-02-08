#!/usr/bin/python3
"""
   New User object that handles all
   default RESTFul API actions
"""
from flask import request
from api.v1.app import *
from api.v1.views.index import *
from models.user_model import User
from models import storage
import json


# @app_views.route('/user/register', methods=['GET'], strict_slashes=False)
# def get_user():
#     """Create a new object User"""
#     return jsonify({"Register": "Ok"}), 200
@app_views.route('/user/register', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new object User"""
    # return jsonify({"Register": "Ok"}), 200
    request_data = request.get_json()
    if not request_data:
        return error_handler_400("Not a JSON")

    if 'email' not in request_data:
        return error_handler_400("Missing email")

    elif 'password' not in request_data:
        return error_handler_400("Missing password")

    information = dict(request_data)
    new_user = User(**information)
    storage.new(new_user)

    new_json = json.dumps(new_user.to_dict())
    storage.save()
    return new_json, 201


@app_views.route('/user/login', methods=['GET'], strict_slashes=False)
def login_user():
    """Update information of an object User by id"""
    # return jsonify({"Login": "Ok"}), 200

    object = storage.get(User, user_id)
    if object is None:
        return error_handler_404(object)

    request_data = request.get_json()
    if not request_data:
        return error_handler_400("Not a JSON")

    ignore = ["id", "created_at", "updated_at", "email"]
    for key, value in dict(request_data).items():
        if key not in ignore:
            setattr(object, key, value)

    new_json = json.dumps(object.to_dict())
    storage.save()
    return new_json, 200
