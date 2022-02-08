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
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
import json
import hashlib


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_user():
    """Return json file with all USERS"""
    new_dict = storage.all('User')
    new_array = []
    for user in new_dict.values():
        new_array.append(user.to_dict())
    return json.dumps(new_array)

@app_views.route('/user/register', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new object User"""
    request_data = request.get_json()
    if not request_data:
        return error_handler_400("Not a JSON")
    if 'mail' not in request_data:
        return error_handler_400("Missing email")

    elif 'password' not in request_data:
        return error_handler_400("Missing password")

    new_user = User(**request_data)
    storage.new(new_user)

    new_json = json.dumps(new_user.to_dict())
    storage.save()
    return new_json, 201

@app_views.route('/user/login', methods=['POST'], strict_slashes=False)
def login_user():
    """Update information of an object User by id"""

    request_data = request.get_json()
    if not request_data:
        return error_handler_400("Not a JSON")
    pwd = hashlib.md5(request_data['password'].encode()).hexdigest()
    print(pwd)
    object = storage.get_login(User, request_data['mail'], pwd)
    if object is None:
        return jsonify({"msg": "Bad mail or password, user not found"}), 401

    access_token = create_access_token(identity=request_data['mail'])
    return jsonify(access_token=access_token)

@app_views.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
