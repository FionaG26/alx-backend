#!/usr/bin/env python3
"""
2. Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Configuration for Babel


class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best matched language for the request.

    Returns:
        str: The best matched language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home_page() -> str:
    """Render the home/index page.

    Returns:
        str: The rendered HTML page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
