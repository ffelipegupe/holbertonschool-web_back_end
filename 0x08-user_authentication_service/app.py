#!/usr/bin/env python3
""" Flask App module
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def message() -> str:
    """ Method that returns a JSON payload """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register():
    """ Registers a User """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"}), 200


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def sessions() -> str:
    """ Creates a new session for the user """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        res = jsonify({"email": email, "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")