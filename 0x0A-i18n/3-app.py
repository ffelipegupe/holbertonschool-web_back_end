#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Babel config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """ Home rendering """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """ Function to determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
