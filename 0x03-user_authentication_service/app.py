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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
