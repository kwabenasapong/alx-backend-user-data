#!/usr/bin/env python3

"""Basic flask app
In this task, you will set up a basic Flask app.

Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
# from flask_cors import (CORS, cross_origin)
# from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False
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
    Returns:
        str: [JSON payload]
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not auth.valid_login(email, password):
        abort(401)
    session_id = auth.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
