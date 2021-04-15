#!/usr/bin/env python3
""" Flask App module
"""
from flask import Flask, jsonify, request, redirect, abort
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


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
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


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """ Logs out a User """
    session_id = request.cookies.get("session_id")
    src = AUTH.get_user_from_session_id(session_id)
    if not session_id or not src:
        abort(403)
    AUTH.destroy_session(src.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """ Fecthes the profile ussing a session_id """
    session_id = request.cookies.get("session_id")
    src = AUTH.get_user_from_session_id(session_id)
    if not session_id or not src:
        abort(403)
    return jsonify({"email": src.email}), 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """ Method to get a password token """
    email = request.form.get("email")
    session = AUTH.create_session(email)
    if session is None:
        abort(403)
    tkn = AUTH.get_reset_password_token(email)
    return ({"email": email, "reset_token": tkn})


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """ Method that updates user's password """
    email = request.form.get("email")
    tkn = request.form.get("reset_token")
    new_pwd = request.form.get("new_password")

    try:
        AUTH.update_password(tkn, new_pwd)
    except Exception:
        abort(403)

    return jsonify({"email": src.email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
