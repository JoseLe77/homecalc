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

    # ---- Database nav buttons SQL Query ----
    webcall = open('src/db/webcalls/nav_buttons.sql', mode='r')
    nav_buttons_query = webcall.read()
    webcall.close()
    try:
        cursor.execute(nav_buttons_query)
        nav_buttons_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error al ejecutar la query: {e}")
    finally:
        return nav_buttons_query_results
        connection.close()

def years_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database year list SQL Query ----
    webcall = open('src/db/webcalls/years.sql', mode='r')
    years_list = webcall.read()
    webcall.close()
    try:
        cursor.execute(years_list)
        years_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Years query: {e}") 
    finally:
        return years_list_query_results
        connection.close()

def months_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database month list SQL Query ----
    webcall = open('src/db/webcalls/months.sql', mode='r')
    months_list = webcall.read()
    webcall.close()
    try:
        cursor.execute(months_list)
        months_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Months query: {e}") 
    finally:
        return months_list_query_results
        connection.close()

def periodicity_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database month list SQL Query ----
    webcall = open('src/db/webcalls/expenses/expenses_periodicity.sql', mode='r')
    periodicity_list = webcall.read()
    webcall.close()
    try:
        cursor.execute(periodicity_list)
        periodicity_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at periodicity query: {e}") 
    finally:
        return periodicity_list_query_results
        connection.close()

def expenses_concept_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database month list SQL Query ----
    webcall = open('src/db/webcalls/expenses/expenses_concepts.sql', mode='r')
    expenses_concepts_list = webcall.read()
    webcall.close()
    try:
        cursor.execute(expenses_concepts_list)
        expenses_concepts_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at expenses concepts query: {e}") 
    finally:
        return expenses_concepts_list_query_results
        connection.close()
    
def basic_finance_data():
    if request.method == 'POST':
        year2filter = int(request.form['año'])
        month2filter = int(request.form['mes'])
    else:
        now = datetime.datetime.now()
        year2filter = int(now.year)
        month2filter = int(now.month)

    connection, cursor = dbconnection()
    # print('DB connected successfully')

    # ---- Database SQL Query ----
    if month2filter == 0:
        webcall = open('src/db/webcalls/finance/basic_finance_data_by_YY.sql', mode='r')
    else:
        webcall = open('src/db/webcalls/finance/basic_finance_data_by_YYMM.sql', mode='r')
        
    basic_data_query = webcall.read()
    webcall.close()
    basic_data_query = basic_data_query.format(year2filter, month2filter)
        
    try:
        cursor.execute(basic_data_query)
        basic_data_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at basic finance data SQL query: {e}")    
    finally:
        return basic_data_query_results
        connection.close()


@app.route("/")
def home():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()
    
    return render_template('home.html', nav_buttons_query_results=nav_buttons_query_results)


@app.route("/form")
def form():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()
        
    return render_template('form.html', nav_buttons_query_results=nav_buttons_query_results)

# ---- INCOME ----   

@app.route("/income", methods=['GET', 'POST'])
def income():

    # ---- Database years list SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database SQL Query ----
    years_list_query_results = years_list()

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()

    # ---- Database basic finance data SQL Query ----
    basic_data_query_results = basic_finance_data()
        
    return render_template('incomes/income.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, basic_data_query_results=basic_data_query_results)

# ---- EXPENSES ---- 

@app.route("/expenses", methods=['GET', 'POST'])
def expenses():
    # ---- Database years list SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database SQL Query ----
    years_list_query_results = years_list()

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()

    # ---- Database basic finance data SQL Query ----
    basic_data_query_results = basic_finance_data()
    
    return render_template('expenses/expenses.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, basic_data_query_results=basic_data_query_results)

@app.route("/periodic_expenses", methods=['GET', 'POST'])
def periodic_expenses():
     # ---- Database Menu buttons SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database expenses concepts list SQL Query ----
    expenses_concepts_list_query_results = expenses_concept_list()

    # ---- Database periodicity list SQL Query ----
    periodicity_list_query_results = periodicity_list()

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()
    
    if request.method == 'POST':
        concept2filter = request.form['concepto']
        periodicity2filter = request.form['periodicidad']
        month2filter = int(request.form['mes'])
    else:
        now = datetime.datetime.now()
        month2filter = int(now.month)
        concept2filter = 'TODOS'
        periodicity2filter = 'X'
    
    print(f'Concepto: {concept2filter}')
    print(f'Periodicidad: {periodicity2filter}')
    print(f'Mes: {month2filter}')

    connection, cursor = dbconnection()
    # print('DB connected successfully')
    
    if month2filter==0:
        if periodicity2filter == 'X':
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/periodic_expenses_all.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query
            else:
                webcall = open('src/db/webcalls/expenses/periodic_expenses_all_by_concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(concept2filter)
        else:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/periodic_expenses_all_by_periodicity.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(periodicity2filter)
            else:
                webcall = open('src/db/webcalls/expenses/periodic_expenses_all_by_concept-periodicity.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(concept2filter, periodicity2filter)   
    else:
        if periodicity2filter == 'X':
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/periodic_expenses_by_month.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(month2filter)
            else:
                webcall = open('src/db/webcalls/expenses/periodic_expenses_by_month-concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(concept2filter, month2filter, concept2filter)
        else:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/periodic_expenses_by_month-periodicity.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(periodicity2filter, month2filter, periodicity2filter)
            else:
                webcall = open('src/db/webcalls/expenses/periodic_expenses_by_month-concept-periodicity.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(concept2filter, periodicity2filter, month2filter, concept2filter, periodicity2filter, month2filter)
        
    try:
        cursor.execute(readed_query_2_execute)
        readed_query_executed_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at basic finance data SQL query: {e}")    
    finally:
        connection.close()

    return render_template('expenses/periodic_expenses.html', nav_buttons_query_results=nav_buttons_query_results, expenses_concepts_list_query_results=expenses_concepts_list_query_results, periodicity_list_query_results=periodicity_list_query_results, months_list_query_results=months_list_query_results, readed_query_executed_results =readed_query_executed_results, month2filter=month2filter, concept2filter=concept2filter, periodicity2filter=periodicity2filter)

# ---- ABOUT ---- 

@app.route("/about")
def about():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()
    
    return render_template('about.html', nav_buttons_query_results=nav_buttons_query_results)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5200)

# config.py
DEVELOPMENT = {
    'DEBUG': True,
    'HOST': '127.0.0.1',
    'PORT': 5200
}