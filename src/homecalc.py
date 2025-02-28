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

def dbconnection():
  # Connects to the specified SQLite database and returns a connection and cursor.
  connection = sqlite3.connect('src/db/database/homecalc.db')
  cursor = connection.cursor()
  return connection, cursor
  

""" def tmpl_show_menu():
    return render_template_string(
        '''
        {%- for item in current_menu.children %}
            {% if item.active %}*{% endif %}{{ item.text }}
        {% endfor -%}
        '''
    ) """

# ReDefinir la variable nav_buttons_query_results
nav_buttons_query_results = None

def nav_buttons():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database SQL Query ----
    webcall = open('src/db/webcalls/nav_buttons.sql', mode='r')
    nav_buttons_query = webcall.read()
    webcall.close()
    try:
        cursor.execute(nav_buttons_query)
        nav_buttons_query_results = cursor.fetchall()
        print(nav_buttons_query_results)
    except Exception as e:
        print(f"Error al ejecutar la query: {e}")
    finally:
        return nav_buttons_query_results


@app.route("/")
def home():
    # ---- Database Connection ----
    connection, cursor = dbconnection()
    # print('DB connected successfully')

    # ---- Database SQL Query ----
    webcall = open('src/db/webcalls/nav_buttons.sql', mode='r')
    nav_buttons_query = webcall.read()
    webcall.close()
    try:
        cursor.execute(nav_buttons_query)
        nav_buttons_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error al ejecutar la query: {e}")
    finally:
        # ---- Database SQL Query ----
        webcall = open('src/db/webcalls/must_haveto.sql', mode='r')
        must_haveto_query = webcall.read()
        webcall.close()
        try:
            cursor.execute(must_haveto_query)
            must_haveto_query_results = cursor.fetchall()
        except Exception as e:
            print(f"Error al ejecutar la query: {e}")

    return render_template('home.html', must_haveto_query_results=must_haveto_query_results, nav_buttons_query_results=nav_buttons_query_results)


@app.route("/form")
def form():
    connection, cursor = dbconnection()
    # print('DB connected successfully')

    # ---- Database SQL Query ----
    webcall = open('src/db/webcalls/nav_buttons.sql', mode='r')
    nav_buttons_query = webcall.read()
    webcall.close()
    try:
        cursor.execute(nav_buttons_query)
        nav_buttons_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error al ejecutar la query: {e}")
        
    return render_template('form.html', nav_buttons_query_results=nav_buttons_query_results)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5100)

# config.py
DEVELOPMENT = {
    'DEBUG': True,
    'HOST': '127.0.0.1',
    'PORT': 5100
}