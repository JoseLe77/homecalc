# -------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, session, flash, render_template_string
# import pysqlite3

# -------------------------------------------------------------------------
# Setup
# -------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "homecalc2025"

""" def dbconnection():
  # Connects to the specified SQLite database and returns a connection and cursor.
  connection = sqlite3.connect('../src/db/database/homecalc.db')
  cursor = connection.cursor()
  return connection, cursor """

""" def tmpl_show_menu():
    return render_template_string(
        '''
        {%- for item in current_menu.children %}
            {% if item.active %}*{% endif %}{{ item.text }}
        {% endfor -%}
        '''
    ) """

""" @app.route("/")
def home():
    return render_template('../src/templates/base.html') """


@app.route("/")
def hello_world():
    return render_template('/templates/app.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

# config.py
DEVELOPMENT = {
    'DEBUG': True,
    'HOST': '127.0.0.1',
    'PORT': 5000,
}