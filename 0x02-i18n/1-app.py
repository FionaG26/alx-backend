#!/usr/bin/env python3
"""
1. Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Configuration for Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: The rendered HTML page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
