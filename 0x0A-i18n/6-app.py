#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, g, request
from flask_babel import Babel
from typing import Union


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Babel config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('6-app.Config')


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """ Home rendering """
    return render_template("6-index.html")


@babel.localeselector
def get_locale() -> str:
    """ Function to determine the best match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Function  that returns a user dictionary or None if the ID cannot be
        found or if login_as was not passed.
    """
    user_id = request.args.get("login_as")
    if user_id:
        u_id = int(user_id)
        if u_id in users:
            return users.get(u_id)
    else:
        return None


@app.before_request
def before_request():
    """ Function to find a user and set it as a global
    """
    user = get_user()
    g.user = user


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
