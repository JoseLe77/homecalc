# -------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, session, flash, render_template_string
import sqlite3

# -------------------------------------------------------------------------
# Setup
# -------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "homecalc2025"


@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

# config.py
DEVELOPMENT = {
    'DEBUG': True,
    'HOST': '0.0.0.0',
    'PORT': 4000,
}