# -------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, session, flash, render_template_string
import sqlite3
import datetime

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
    

    return render_template('home.html', nav_buttons_query_results=nav_buttons_query_results)


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

@app.route("/income")
def income():
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
    
        
    return render_template('income.html', nav_buttons_query_results=nav_buttons_query_results)

@app.route("/expenses", methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        year2filter = int(request.form['selected_year'])
        print(year2filter)
        month2filter = int(request.form['mes'])
        print(month2filter)
    else:
        now = datetime.datetime.now()
        year2filter = int(now.year)
        print(year2filter)
        month2filter = int(now.month)
        print(month2filter)

        connection, cursor = dbconnection()
        # print('DB connected successfully')

        # ---- Database SQL Query ----
        webcall = open('src/db/webcalls/nav_buttons.sql', mode='r')
        nav_buttons_query = webcall.read()
        webcall.close()

        # ---- Database SQL Query ----
        webcall = open('src/db/webcalls/years.sql', mode='r')
        years_list = webcall.read()
        webcall.close()

        # ---- Database SQL Query ----
        webcall = open('src/db/webcalls/months.sql', mode='r')
        months_list = webcall.read()
        webcall.close()

        # ---- Database SQL Query ----
        webcall = open('src/db/webcalls/expenses/must_haveto.sql', mode='r')
        must_haveto_query = webcall.read()
        webcall.close()
        must_haveto_query = must_haveto_query.format(year2filter, month2filter)
            
        try:
            cursor.execute(nav_buttons_query)
            nav_buttons_query_results = cursor.fetchall()

            cursor.execute(years_list)
            years_list_query_results = cursor.fetchall()

            cursor.execute(months_list)
            months_list_query_results = cursor.fetchall()

            cursor.execute(must_haveto_query)
            must_haveto_query_results = cursor.fetchall()

        except Exception as e:
            print(f"Error al ejecutar la query: {e}")
        
        finally:
            connection.close()
        
        return render_template('expenses.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, must_haveto_query_results=must_haveto_query_results)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5200)

# config.py
DEVELOPMENT = {
    'DEBUG': True,
    'HOST': '127.0.0.1',
    'PORT': 5200
}