#!/usr/bin/env python3

""" File that handles all routes for the Session authentication """

from flask import request, jsonify, abort, make_response
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ handles all routes for the session authentication """

    email = request.form.get('email')
    password = request.form.get('password')
    users = User.search({'email': email})

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = make_response(user.to_join())
    response.set_cookie(getenv('SESSION_NAME'), session_id)

    return response

@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ create logout method with delete method """
    from api.v1.app import auth

    if auth.destroy_session(request) is False:
        abort(404)

    return jsonify({}), 200
