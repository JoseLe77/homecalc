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

def yearslist2filter():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database year list SQL Query ----
    webcall = open('src/db/webcalls/get_year_2_filter.sql', mode='r')
    years_list_2_filter = webcall.read()
    webcall.close()
    try:
        cursor.execute(years_list_2_filter)
        years_list_2_filter_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Years 2 filter query: {e}") 
    finally:
        return years_list_2_filter_query_results
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

def extra_expenses_concept_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database month list SQL Query ----
    webcall = open('src/db/webcalls/expenses/extra_expenses_concepts.sql', mode='r')
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
  
def monthintext():
    if request.method == 'POST':
        year2filter = int(request.form['año'])
        print(year2filter)
        month2filter = int(request.form['mes'])
        print(month2filter)
    else:
        now = datetime.datetime.now()
        year2filter = int(now.year)
        month2filter = int(now.month)

    if month2filter == 0:
        filtered_month = 'Mes (TODOS)'
    else:
        webcall = open('src/db/webcalls/get_text_month.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(month2filter)
        try:
            connection, cursor = dbconnection()
            cursor.execute(readed_query_2_execute)
            readed_query_executed_results = cursor.fetchone()

        except Exception as e:
            print(f"Error at filtered month data SQL query: {e}")    
        finally:
            filtered_month = f'Mes ({readed_query_executed_results[0]})'
            connection.close()

    filtered_month = filtered_month

    filtered_year = f'Año ({year2filter})'
    
    Filtrered_data = f'{filtered_year} y {filtered_month}.'

    return Filtrered_data

# ---- HOME ----  
@app.route("/")
def home():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()
    
    return render_template('home.html', nav_buttons_query_results=nav_buttons_query_results)

# ---- FORM ----  
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
    
    filtered_data = monthintext()
        
    return render_template('incomes/income.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, basic_data_query_results=basic_data_query_results, filtered_data=filtered_data)

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

    Filtrered_data = monthintext()
    
    return render_template('expenses/expenses.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, basic_data_query_results=basic_data_query_results, Filtrered_data=Filtrered_data)

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

    if month2filter == 0:
        filtered_month = 'Mes (TODOS)'
    else:
        webcall = open('src/db/webcalls/get_text_month.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(month2filter)

        try:
            connection, cursor = dbconnection()
            cursor.execute(readed_query_2_execute)
            readed_query_executed_results = cursor.fetchone()
        except Exception as e:
            print(f"Error at filtered month data SQL query: {e}")    
        finally:
            connection.close()
        filtered_month = f'Mes ({readed_query_executed_results[0]})'

    if periodicity2filter == 'X':
        filtered_periodicity = 'Periodicidad (TODOS)'
    else:
        webcall = open('src/db/webcalls/get_text_periodicity.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(periodicity2filter)

        try:
            connection, cursor = dbconnection()
            cursor.execute(readed_query_2_execute)
            readed_query_executed_results = cursor.fetchone()
        except Exception as e:
            print(f"Error at filtered periodicity data SQL query: {e}")    
        finally:
            connection.close()
        filtered_periodicity = f'{readed_query_executed_results[0]}'

    if concept2filter == 'TODOS':
        filtered_concept = 'Concepto (TODOS)'
    else:
        filtered_concept = f'Concepto ({concept2filter})'
    

    Filtrered_data = f'{filtered_concept},  {filtered_periodicity} y {filtered_month}.'

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
                readed_query_2_execute = readed_query.format(month2filter,concept2filter, periodicity2filter, month2filter)
        
    try:
        cursor.execute(readed_query_2_execute)
        readed_query_executed_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at basic finance data SQL query: {e}")    
    finally:
        connection.close()

    return render_template('expenses/periodic_expenses.html', nav_buttons_query_results=nav_buttons_query_results, expenses_concepts_list_query_results=expenses_concepts_list_query_results, periodicity_list_query_results=periodicity_list_query_results, months_list_query_results=months_list_query_results, readed_query_executed_results =readed_query_executed_results, month2filter=month2filter, concept2filter=concept2filter, periodicity2filter=periodicity2filter, Filtrered_data=Filtrered_data)

@app.route("/extra_expenses", methods=['GET', 'POST'])
def extra_expenses():
     # ---- Database Menu buttons SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database expenses concepts list SQL Query ----
    expenses_concepts_list_query_results = extra_expenses_concept_list()

    # ---- Database year list SQL Query ----
    years_list_query_results = yearslist2filter()

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()

    # Get data from form, first charge will get actual month and actual year
    if request.method == 'POST':
        concept2filter = request.form['concepto']
        year2filter = request.form['año']
        month2filter = int(request.form['mes'])
    else:
        now = datetime.datetime.now()
        year2filter = int(now.year)
        month2filter = int(now.month)
        concept2filter = 'TODOS'

    # will get number month and translate it to text (Example. 6 = JUNE)
    if month2filter == 0:
        filtered_month = 'Mes (TODOS)'
    else:
        webcall = open('src/db/webcalls/get_text_month.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(month2filter)

        try:
            connection, cursor = dbconnection()
            cursor.execute(readed_query_2_execute)
            readed_query_executed_results = cursor.fetchone()
        except Exception as e:
            print(f"Error at filtered month data SQL query: {e}")    
        finally:
            connection.close()
        filtered_month = f'Mes ({readed_query_executed_results[0]})'

    if year2filter == 'TODOS':
        filtered_year = 'Año (TODOS)'
    else:
        filtered_year = f'Año ({year2filter})'

    if concept2filter == 'TODOS':
        filtered_concept = 'Concepto (TODOS)'
    else:
        filtered_concept = f'Concepto ({concept2filter})'
    
    Filtered_data = f'{filtered_concept},  {filtered_year} y {filtered_month}.'

    print(year2filter)
    print(type(year2filter))
    print(month2filter)
    print(type(month2filter))
    print(concept2filter)
    print(type(concept2filter))

    connection, cursor = dbconnection()
    print('DB connected successfully')

    if year2filter == 'TODOS':
        if month2filter == 0:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/extra_expenses_all.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query
            else:
                webcall = open('src/db/webcalls/expenses/extra_expenses_all_by_concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(concept2filter)
        else:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_month.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(month2filter)
            else:
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_month-concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(month2filter, concept2filter)
    else:
        if month2filter == 0:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter))
            else:
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year-concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter), concept2filter)
        else:
            if concept2filter == 'TODOS':
                print('Query por Año y Mes')
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year-month.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter), month2filter)
            else:
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year-month-concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter), month2filter, concept2filter)
    try:
        cursor.execute(readed_query_2_execute)
        readed_query_executed_results = cursor.fetchall()
        print('Query Ejecutada')
    except Exception as e:
        print(f"Error at extra expenses data SQL query: {e}")    
    finally:
        connection.close()

    print(readed_query_executed_results)

    return render_template('expenses/extra_expenses.html', nav_buttons_query_results=nav_buttons_query_results, expenses_concepts_list_query_results=expenses_concepts_list_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, year2filter=year2filter, month2filter=month2filter, concept2filter=concept2filter, Filtered_data=Filtered_data, readed_query_executed_results=readed_query_executed_results)

# ---- ABOUT ---- 
@app.route("/about")
def about():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()
    
    return render_template('about.html', nav_buttons_query_results=nav_buttons_query_results)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5200)

# ---- CONFIG ----
DEVELOPMENT = {
    'DEBUG': True,
    'HOST': '127.0.0.1',
    'PORT': 5200
}