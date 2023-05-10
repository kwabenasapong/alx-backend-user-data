#!/usr/bin/env python3

"""Basic flask app
In this task, you will set up a basic Flask app.

Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from flask_cors import (CORS, cross_origin)
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = Auth()


@app.route('/', methods=['GET'])
def basic_route() -> str:
    """Basic route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """Users route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """User Login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        check_user = auth.valid_login(email, password)
        user = auth.register_user(email, password)
        session_id = auth.create_session(email)
        return jsonify({"email": user.email, "message": "logged in"})
    except Exception:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
