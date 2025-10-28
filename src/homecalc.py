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
        connection.close()
        return nav_buttons_query_results

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
        connection.close()
        return years_list_query_results

def income_years_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database year list SQL Query ----
    webcall = open('src/db/webcalls/income/income_years.sql', mode='r')
    years_list = webcall.read()
    webcall.close()
    try:
        cursor.execute(years_list)
        years_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Years query: {e}") 
    finally:
        connection.close()
        return years_list_query_results
    
def income_periodic_companies_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database year list SQL Query ----
    webcall = open('src/db/webcalls/income/income_periodic_companies.sql', mode='r')
    companies_list = webcall.read()
    webcall.close()
    try:
        cursor.execute(companies_list)
        periodic_companies_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Years query: {e}") 
    finally:
        connection.close()
        return periodic_companies_list_query_results

def income_extra_companies_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database year list SQL Query ----
    webcall = open('src/db/webcalls/income/income_extra_companies.sql', mode='r')
    companies_list = webcall.read()
    webcall.close()
    try:
        cursor.execute(companies_list)
        extra_companies_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Years query: {e}") 
    finally:
        connection.close()
        return extra_companies_list_query_results

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
        connection.close()
        return years_list_2_filter_query_results

def months_list():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database month list SQL Query ----
    webcall = open('src/db/webcalls/months.sql', mode='r')
    months_list = webcall.read()
    webcall.close()
    months_list_query_results = []
    try:
        cursor.execute(months_list)
        months_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Months query: {e}") 
    finally:
        connection.close()
    return months_list_query_results

def months_list_selected():
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database month list SQL Query ----
    webcall = open('src/db/webcalls/months_selected.sql', mode='r')
    months_list = webcall.read()
    months_list_query = months_list.format(expense_month, expense_month)
    webcall.close()
    try:
        cursor.execute(months_list_query)
        months_list_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Months query: {e}") 
    finally:
        connection.close()
        return months_list_query_results

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
        connection.close()
        return periodicity_list_query_results

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
        connection.close()
        return expenses_concepts_list_query_results

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
        connection.close()
        return expenses_concepts_list_query_results

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
        connection.close()
        return basic_data_query_results
  
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

@app.route("/periodic_income")
def periodic_income():
    # ---- Database buttons list SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database years SQL Query ----
    years_list_query_results = income_years_list()

    # ---- Database companies SQL Query ----
    periodic_companies_list_query_results = income_periodic_companies_list()

    return render_template('incomes/periodic_income.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, periodic_companies_list_query_results=periodic_companies_list_query_results)

@app.route("/periodic_income_filter", methods=['GET', 'POST'])
def periodic_income_filter():
    if request.method == 'POST':
        company2filter = request.form['company']
        year2filter = request.form['año']

     # ---- Database buttons list SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database years SQL Query ----
    years_list_query_results = income_years_list()

    # ---- Database companies SQL Query ----
    periodic_companies_list_query_results = income_periodic_companies_list()
    
    # ---- Database Connection ----
    connection, cursor = dbconnection()

    # ---- Database periodic filtered income list SQL Query ----
    webcall = open('src/db/webcalls/income/income_periodic_anual.sql', mode='r')
    periodic_query = webcall.read()
    webcall.close()
    readed_query_2_execute = periodic_query.format(company2filter, year2filter)
    try:
        cursor.execute(readed_query_2_execute)
        periodic_income_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Years query: {e}") 
    finally:
        connection.close()

    return render_template('incomes/periodic_income.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, periodic_companies_list_query_results=periodic_companies_list_query_results, periodic_income_query_results=periodic_income_query_results)

@app.route("/extra_income")
def extra_income():
    # ---- Database buttons list SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database years SQL Query ----
    years_list_query_results = income_years_list()

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()

    # ---- Database companies SQL Query ----
    extra_companies_list_query_results = income_extra_companies_list()

    return render_template('incomes/extra_income.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results,extra_companies_list_query_results=extra_companies_list_query_results)

@app.route('/extra_income_filter', methods=['GET', 'POST'])
def extra_income_filter():
    if request.method == 'POST':
        company2filter = request.form['company']
        year2filter = request.form['año']
        month2filter = request.form['mes']

    # ---- Database buttons list SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database years SQL Query ----
    years_list_query_results = income_years_list()

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()

    # ---- Database companies SQL Query ----
    extra_companies_list_query_results = income_extra_companies_list()

    # ---- Database Connection ----
    connection, cursor = dbconnection()

    if company2filter == 'TODAS' and month2filter == '0':
        # ---- Database extra filtered income  all SQL Query ----
        webcall = open('src/db/webcalls/income/income_extra_anual.sql', mode='r')
        extra_query = webcall.read()
        webcall.close()
        readed_query_2_execute = extra_query.format(year2filter)
    elif company2filter != 'TODAS' and month2filter == '0':
        # ---- Database extra filtered income  by month SQL Query ----
        webcall = open('src/db/webcalls/income/income_extra_anual_by_company.sql', mode='r')
        extra_query = webcall.read()
        webcall.close()
        readed_query_2_execute = extra_query.format(company2filter, year2filter)
    elif company2filter == 'TODAS' and month2filter != '0':
        # ---- Database extra filtered income  by month SQL Query ----
        webcall = open('src/db/webcalls/income/income_extra_anual_by_month.sql', mode='r')
        extra_query = webcall.read()
        webcall.close()
        readed_query_2_execute = extra_query.format(year2filter, month2filter)
    else:
        # ---- Database extra filtered income liby company and month SQL Query ----
        webcall = open('src/db/webcalls/income/income_extra_anual_by_company_month.sql', mode='r')
        extra_query = webcall.read()
        webcall.close()
        readed_query_2_execute = extra_query.format(company2filter, year2filter, month2filter)

    try:
        cursor.execute(readed_query_2_execute)
        extra_income_query_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at Years query: {e}") 
    finally:
        connection.close()

    return render_template('incomes/extra_income.html', nav_buttons_query_results=nav_buttons_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results,extra_companies_list_query_results=extra_companies_list_query_results, extra_income_query_results=extra_income_query_results)

@app.route("/manage_incomes")
def manage_incomes():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database income periodic companies list SQL Query ----
    periodic_companies_list_query_results = income_periodic_companies_list()

    # ---- Database income periodic companies list SQL Query ----
    extra_companies_list_query_results = income_extra_companies_list()[1:]

    # ---- Database year list SQL Query ----
    years_list_query_results = yearslist2filter()[1:]

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()
    
    income_types_descriptions = { 'P': 'Ingresos Periodicos', 'E': 'Ingresos Extraordinarios' }

    return render_template('incomes/manage_incomes.html', nav_buttons_query_results=nav_buttons_query_results, periodic_companies_list_query_results=periodic_companies_list_query_results, extra_companies_list_query_results=extra_companies_list_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, income_types_descriptions=income_types_descriptions)

@app.route("/record_income")
def record_income():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database income periodic companies list SQL Query ----
    periodic_companies_list_query_results = income_periodic_companies_list()

    # ---- Database income periodic companies list SQL Query ----
    extra_companies_list_query_results = income_extra_companies_list()[1:]

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()[1:]
    
    return render_template('incomes/record_income.html', nav_buttons_query_results=nav_buttons_query_results, periodic_companies_list_query_results=periodic_companies_list_query_results, extra_companies_list_query_results=extra_companies_list_query_results, months_list_query_results=months_list_query_results)

@app.route("/add_income", methods=['GET','POST'])
def add_income():
    if request.method == 'POST':
        tipo = request.form['tipo']
        año = request.form['año']
        cantidad = request.form['cantidad']
        cantidad = cantidad.replace(',', '.')
        if tipo == 'P':
            company = request.form['company_periodic']
            paga_extra = request.form['paga_extra']
            mes_desde= request.form['mes_desde']
            mes_hasta= request.form['mes_hasta']
            irpf = request.form['irpf']
            irpf = irpf.replace(',', '.')
            resto_impuestos = request.form['resto_impuestos']
            resto_impuestos = resto_impuestos.replace(',', '.')
            bonus = request.form['bonus']
            bonus = bonus.replace(',', '.') 
        else:
            company = request.form['company_extra']
            concepto = request.form['concepto']
            mes = request.form['mes']
        
    connection, cursor = dbconnection()
    # print('DB connected successfully')

    # ---- Database add income SQL Query ----
    if (tipo == 'P'):
        if paga_extra == 'S':
            paga_extra_value = 1
        else:
            paga_extra_value = 0

        mensualidades = int(mes_hasta) - int(mes_desde) +  paga_extra_value
        webcall = open('src/db/webcalls/income/add_periodic_income.sql', mode='r')
        add_periodic_income_query = webcall.read()
        webcall.close()
        add_income_query_2_execute = add_periodic_income_query.format(company, año, mes_desde, mes_hasta, cantidad, mensualidades)
        webcall = open('src/db/webcalls/income/add_periodic_income_calculation.sql', mode='r')
        add_periodic_income_calculation_query = webcall.read()
        webcall.close()
        webcall = open('src/db/webcalls/income/add_periodic_salary_discounts.sql', mode='r')
        add_periodic_income_salary_discount_query = webcall.read()
        webcall.close()

    else:
        webcall = open('src/db/webcalls/income/add_extra_income.sql', mode='r')
        add_extra_income_query = webcall.read()
        webcall.close()
        add_income_query_2_execute = add_extra_income_query.format(company, año, mes, cantidad, concepto)
        
    try:
        cursor.execute(add_income_query_2_execute)
        connection.commit()
        if (tipo == 'P'):
            cursor.execute(add_periodic_income_calculation_query)
            anual_salary_up = cursor.fetchone()[0]
            print(anual_salary_up)
            neto_anual = 100 - (float(irpf) + float(resto_impuestos))
            print(neto_anual)
            cursor.execute(add_periodic_income_salary_discount_query.format(company, año, anual_salary_up, neto_anual, irpf, resto_impuestos, bonus))
            connection.commit()
    except Exception as e:
        print(f"Error at add income SQL query: {e}")    
    finally:
        connection.close()
    
    return redirect(url_for('record_income'))

@app.route("/manage_income_filter", methods=['GET', 'POST'])
def manage_income_filter():
    if request.method == 'POST':
        tipo = request.form['tipo']
        año = request.form['año']
        if tipo == 'P':
            company = request.form['company_periodic']
        else:
            company = request.form['company_extra'] 
            mes = request.form['mes']
    
    # ---- Database SQL Query ----
    if tipo == 'P':
        webcall = open('src/db/webcalls/income/income_periodic_anual_2_edit.sql', mode='r')
        periodic_query = webcall.read()
        webcall.close()
        readed_query_2_execute = periodic_query.format(company, año)
        filtered_data = f'Ingreso Periodico por Compañia ({company}) y año ({año}).'
    else:
        if mes == '0':
            webcall = open('src/db/webcalls/income/income_extra_anual.sql', mode='r')
            extra_query = webcall.read()
            webcall.close()
            readed_query_2_execute = extra_query.format(año)
            filtered_data = f'Ingreso Extraordinario por año ({año}).'
        else:
            webcall = open('src/db/webcalls/income/income_extra_anual_by_company_month.sql', mode='r')
            extra_query = webcall.read()
            webcall.close()
            readed_query_2_execute = extra_query.format(company, año, mes)
            filtered_data = f'Ingreso Extraordinario por compañia ({company}), mes ({mes}) y año ({año}).'
    
    connection, cursor = dbconnection()
    try:
        cursor.execute(readed_query_2_execute)
        income_query_results = cursor.fetchall()
        print(income_query_results)
    except Exception as e:
        print(f"Error at filtered income query: {e}")
    finally:
        connection.close()
    
     # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database income periodic companies list SQL Query ----
    periodic_companies_list_query_results = income_periodic_companies_list()

    # ---- Database income periodic companies list SQL Query ----
    extra_companies_list_query_results = income_extra_companies_list()[1:]

    # ---- Database year list SQL Query ----
    years_list_query_results = yearslist2filter()[1:]

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()

    income_types_descriptions = { 'P': 'Ingresos Periodicos', 'E': 'Ingresos Extraordinarios' }

    if tipo == 'P':
        income_types_descriptions = income_types_descriptions
    if tipo=='E':
        income_types_descriptions = dict(reversed(list(income_types_descriptions.items())))
    else:
        income_types_descriptions = income_types_descriptions
    

    return render_template('incomes/manage_incomes.html', nav_buttons_query_results=nav_buttons_query_results, periodic_companies_list_query_results=periodic_companies_list_query_results, extra_companies_list_query_results=extra_companies_list_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, income_query_results=income_query_results, filtered_data=filtered_data, income_types_descriptions=income_types_descriptions)

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
                readed_query_2_execute = readed_query.format(month2filter, month2filter)
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

    connection, cursor = dbconnection()
    # print('DB connected successfully')

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
                readed_query_2_execute = readed_query.format(concept2filter,concept2filter)
        else:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_month.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(month2filter, month2filter)
            else:
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_month-concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(month2filter, concept2filter, month2filter, concept2filter)
    else:
        if month2filter == 0:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter), int(year2filter))
            else:
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year-concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter), concept2filter, int(year2filter), concept2filter)
        else:
            if concept2filter == 'TODOS':
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year-month.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter), month2filter, int(year2filter), month2filter)
            else:
                webcall = open('src/db/webcalls/expenses/extra_expenses_by_year-month-concept.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(int(year2filter), month2filter, concept2filter)
    try:
        cursor.execute(readed_query_2_execute)
        readed_query_executed_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at extra expenses data SQL query: {e}")    
    finally:
        connection.close()

    return render_template('expenses/extra_expenses.html', nav_buttons_query_results=nav_buttons_query_results, expenses_concepts_list_query_results=expenses_concepts_list_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, year2filter=year2filter, month2filter=month2filter, concept2filter=concept2filter, Filtered_data=Filtered_data, readed_query_executed_results=readed_query_executed_results)

@app.route("/manage_expenses")
def manage_expenses():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database periodicity list SQL Query ----
    periodicity_list_query_results = periodicity_list()[1:]

    # ---- Database year list SQL Query ----
    years_list_query_results = yearslist2filter()[1:]

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()
    
    return render_template('expenses/manage_expenses.html', nav_buttons_query_results=nav_buttons_query_results, periodicity_list_query_results=periodicity_list_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results)

@app.route("/manage_expenses_filter", methods=['GET', 'POST'])
def manage_expenses_filter():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database periodicity list SQL Query ----
    periodicity_list_query_results = periodicity_list()[1:]

    # ---- Database year list SQL Query ----
    years_list_query_results = yearslist2filter()[1:]

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()

    if request.method == 'POST':
        type2filter = request.form['tipo']
        periodicity2filter = request.form['periodicidad']
        year2filter = request.form['año']
        month2filter = int(request.form['mes'])
        
    connection, cursor = dbconnection()
    # print('DB connected successfully')

    if month2filter is not None:
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

    if type2filter == 'P':
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
            filtered_periodicity = f'{readed_query_executed_results[0]}'

        if periodicity2filter!='M':
            if month2filter==0:
                webcall = open('src/db/webcalls/expenses/periodic_expenses_all_by_periodicity.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(periodicity2filter)
                filtered_data = f'Gasto por {filtered_periodicity}'
            else:
                webcall = open('src/db/webcalls/expenses/periodic_expenses_by_month-periodicity.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(periodicity2filter, month2filter, periodicity2filter)
                filtered_data = f'Gasto por {filtered_periodicity} del {filtered_month}'
        else:
            webcall = open('src/db/webcalls/expenses/periodic_expenses_all_by_periodicity.sql', mode='r')
            readed_query = webcall.read()
            webcall.close()
            readed_query_2_execute = readed_query.format(periodicity2filter)
            filtered_data = f'Gastos por {filtered_periodicity}'
    else:
        if month2filter==0:
            webcall = open('src/db/webcalls/expenses/extra_expenses_by_year_to_edit.sql', mode='r')
            readed_query = webcall.read()
            webcall.close()
            readed_query_2_execute = readed_query.format(int(year2filter))
            filtered_data = f'Gastos Extraordinarios del Año {year2filter}'
        else:
            webcall = open('src/db/webcalls/expenses/extra_expenses_by_year_month_to_edit.sql', mode='r')
            readed_query = webcall.read()
            webcall.close()
            readed_query_2_execute = readed_query.format(int(year2filter), month2filter)
            filtered_data = f'Gastos Extraordinarios por Año {year2filter} y {filtered_month}'

    try:
        cursor.execute(readed_query_2_execute)
        readed_query_executed_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at basic finance data SQL query: {e}")    
    finally:
        connection.close()
        print(readed_query_executed_results)
        print(filtered_data)

    return render_template('expenses/manage_expenses.html', nav_buttons_query_results=nav_buttons_query_results, readed_query_executed_results=readed_query_executed_results,  periodicity_list_query_results=periodicity_list_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results, filtered_data=filtered_data)

@app.route("/record_expenses")
def record_expenses():
    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database periodicity list SQL Query ----
    periodicity_list_query_results = periodicity_list()[1:]

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()[1:]
    
    return render_template('expenses/record_expenses.html', nav_buttons_query_results=nav_buttons_query_results, periodicity_list_query_results=periodicity_list_query_results, months_list_query_results=months_list_query_results)

@app.route("/add_expense", methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        # ----------------
        #    HTML Form
        # ----------------
        year2add = request.form['año']
        print(f'YEAR: {year2add}')
        month2add = request.form['mes']
        #month2add = 'NULL' if month2add == '0' else month2add
        print(f'NONTH: {month2add}')
        concept2add = request.form['concepto']
        print(f'CONCEPT: {concept2add}')
        periodicity2add = request.form['periodicidad']
        print(f'PERIODICITY: {periodicity2add}')
        expenseType = request.form['tipo']
        print(f'TYPE: {expenseType}')
        qty2add = request.form['cantidad']
        qty2add = qty2add.replace(',', '.')
        print(f'QUANTITY: {qty2add}')

        if expenseType == 'P':
            if periodicity2add == 'M':
                if (concept2add is not None and qty2add is not None) or (concept2add != '' and qty2add != '') :
                    webcall = open('src/db/webcalls/expenses/add_periodic_mensual_expenses.sql', mode='r')
                    readed_query = webcall.read()
                    webcall.close()
                    readed_query_2_execute = readed_query.format(concept2add, periodicity2add, float(qty2add))
                else:
                    print('Error1')
            else:
                if month2add is not None and concept2add is not None and qty2add is not None:
                    webcall = open('src/db/webcalls/expenses/add_periodic_expenses.sql', mode='r')
                    readed_query = webcall.read()
                    webcall.close()
                    readed_query_2_execute = readed_query.format(concept2add, periodicity2add, float(qty2add), int(month2add))
                else:
                    print('Error2')
        elif expenseType == 'E':
            if year2add is not None and month2add is not None and concept2add is not None and qty2add is not None:
                webcall = open('src/db/webcalls/expenses/add_extra_expense.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(concept2add, float(qty2add), int(year2add), int(month2add))
            else:
                print('Error3')
        else:
            print(f'Error en filtro de gasto: {expenseType}.')
    
    try:
        connection, cursor = dbconnection()
        cursor.execute(readed_query_2_execute)
        connection.commit()
        connection.close()
        print('ejecutado')
    except Exception as e:
        print(f'Error añadiendo {expenseType}. {e}')

    # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database periodicity list SQL Query ----
    periodicity_list_query_results = periodicity_list()[1:]

    # ---- Database months list SQL Query ----
    months_list_query_results = months_list()
    
    return render_template('expenses/record_expenses.html', nav_buttons_query_results=nav_buttons_query_results, periodicity_list_query_results=periodicity_list_query_results, months_list_query_results=months_list_query_results)

@app.route("/selected_expense/<selected_expense>")
def selected_expense(selected_expense):
    expense_type=selected_expense[:1]
    print(expense_type)
    selected_expense_id=selected_expense[1:]
    print(selected_expense_id)

     # ---- Database SQL Query ----
    nav_buttons_query_results = nav_buttons()

    # ---- Database SQL Query ----
    years_list_query_results = years_list()

    connection, cursor = dbconnection()
    # print('DB connected successfully')

    if expense_type=='E':
        webcall = open('src/db/webcalls/expenses/extra_expense_selected_to_edit.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(selected_expense_id)
    else:
        webcall = open('src/db/webcalls/expenses/periodic_expense_selected_to_edit.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(selected_expense)

    try:
        connection, cursor = dbconnection()
        cursor.execute(readed_query_2_execute)
        readed_query_executed_results = cursor.fetchall()
    except Exception as e:
        print(f"Error at filtered month data SQL query: {e}")    
    finally:
        connection.close()

    if expense_type=='E':
        for result in readed_query_executed_results:
            expense_id = result[0]
            expense_concept = result[1]
            expense_qty = result[2]
            expense_month = result[4]
            expense_year = result[3]
            expense_active = result[5]

        readed_query_executed_results = [expense_id, expense_concept, expense_year, expense_month, expense_qty, expense_active]
        print(readed_query_executed_results)

        # ---- Database Connection ----
        connection, cursor = dbconnection()

        # ---- Database month list SQL Query ----
        webcall = open('src/db/webcalls/months_selected.sql', mode='r')
        months_list = webcall.read()
        months_list_query = months_list.format(expense_month, expense_month)
        webcall.close()
        try:
            cursor.execute(months_list_query)
            months_list_query_results = cursor.fetchall()
        except Exception as e:
            print(f"Error at Months query: {e}") 
        finally:
            connection.close() 
        
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
            connection.close()

    else:
        for result in readed_query_executed_results:
            expense_id = result[0]
            expense_concept = result[1]
            expense_periodicity = result[2]
            expense_qty = result[3]
            expense_month = result[4]
            expense_active = result[5]

        readed_query_executed_results = [expense_id, expense_concept, expense_periodicity, expense_month, expense_qty, expense_active]
        print(readed_query_executed_results)

        if expense_periodicity != 'M':
            # ---- Database months list SQL Query ----
            # ---- Database Connection ----
            connection, cursor = dbconnection()

            # ---- Database month list SQL Query ----
            webcall = open('src/db/webcalls/months_selected.sql', mode='r')
            months_list = webcall.read()
            months_list_query = months_list.format(expense_month, expense_month)
            webcall.close()
            try:
                cursor.execute(months_list_query)
                months_list_query_results = cursor.fetchall()
            except Exception as e:
                print(f"Error at Months query: {e}") 
            finally:
                connection.close()
        else:
            # ---- Database Connection ----
            connection, cursor = dbconnection()

            # ---- Database month list SQL Query ----
            webcall = open('src/db/webcalls/months.sql', mode='r')
            months_list = webcall.read()
            webcall.close()
            months_list_query_results = []
            try:
                cursor.execute(months_list)
                months_list_query_results = cursor.fetchall()
            except Exception as e:
                print(f"Error at Months query: {e}") 
            finally:
                connection.close()
            months_list_query_results = months_list_query_results[1:]
        
        # ---- Database periodicity list SQL Query ----
        # ---- Database Connection ----
        connection, cursor = dbconnection()

        # ---- Database month list SQL Query ----
        webcall = open('src/db/webcalls/expenses/expenses_periodicity_selected.sql', mode='r')
        periodicity_list = webcall.read()
        periodicity_list_query = periodicity_list.format(expense_periodicity, expense_periodicity)
        webcall.close()
        print(periodicity_list_query)
        try:
            cursor.execute(periodicity_list_query)
            periodicity_list_query_results = cursor.fetchall()
        except Exception as e:
            print(f"Error at periodicity query: {e}") 
        finally:
            connection.close()

    if expense_type == 'E':
        return render_template('expenses/edit_selected_expenses.html', expense_type=expense_type, readed_query_executed_results=readed_query_executed_results, nav_buttons_query_results=nav_buttons_query_results, periodicity_list_query_results=periodicity_list_query_results[1:], years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results)
    else:
        return render_template('expenses/edit_selected_expenses.html', expense_type=expense_type, readed_query_executed_results=readed_query_executed_results, nav_buttons_query_results=nav_buttons_query_results,  periodicity_list_query_results=periodicity_list_query_results, years_list_query_results=years_list_query_results, months_list_query_results=months_list_query_results)

@app.route("/update_expense", methods=['GET', 'POST'])
def update_expense():
    if request.method == 'POST':
        # ----------------
        #    HTML Form
        # ----------------
        id2edit = request.form['id']     
        year2edit = request.form['año']
        month2edit = request.form['mes']
        concept2edit = request.form['concepto']
        periodicity2edit = request.form['periodicidad']
        expenseType = request.form['tipo']
        qty2edit = request.form['cantidad']
        qty2edit = qty2edit.replace(',', '.')

        print(f'ID: {id2edit}')
        print(f'YEAR: {year2edit}')
        print(f'MONTH: {month2edit}')
        print(f'CONCEPT: {concept2edit}')
        print(f'PERIODICITY: {periodicity2edit}')
        print(f'TYPE: {expenseType}')
        print(f'QUANTITY: {qty2edit}')

        if expenseType == 'P':
            if periodicity2edit == 'M':
                if (concept2edit is not None and qty2edit is not None) or (concept2edit != '' and qty2edit != '') :
                    webcall = open('src/db/webcalls/expenses/update_periodic_mensual_expenses.sql', mode='r')
                    readed_query = webcall.read()
                    webcall.close()
                    readed_query_2_execute = readed_query.format(concept2edit, periodicity2edit, float(qty2edit), id2edit)
                else:
                    print('Error1')
            else:
                if month2edit is not None and concept2edit is not None and qty2edit is not None:
                    webcall = open('src/db/webcalls/expenses/update_periodic_expenses.sql', mode='r')
                    readed_query = webcall.read()
                    webcall.close()
                    readed_query_2_execute = readed_query.format(concept2edit, periodicity2edit, float(qty2edit), int(month2edit), id2edit)
                else:
                    print('Error2')
        elif expenseType == 'E':
            if year2edit is not None and month2edit is not None and concept2edit is not None and qty2edit is not None:
                webcall = open('src/db/webcalls/expenses/update_extra_expense.sql', mode='r')
                readed_query = webcall.read()
                webcall.close()
                readed_query_2_execute = readed_query.format(concept2edit, float(qty2edit), int(year2edit), int(month2edit), id2edit)
            else:
                print('Error3')
        else:
            print(f'Error en filtro de gasto: {expenseType}.')

    try:
        connection, cursor = dbconnection()
        cursor.execute(readed_query_2_execute)
        connection.commit()
        connection.close()
        print('ejecutado')
    except Exception as e:
        print(f'Error añadiendo {expenseType}. {e}')

    return redirect(url_for('manage_expenses'))

@app.route("/delete_expenses/<expenseid>")
def delete_expenses(expenseid):
    expense_type=expenseid[:1]
    expense_id=expenseid[1:]

    connection, cursor = dbconnection()
    # print('DB connected successfully')

    if expense_type=='E':
        webcall = open('src/db/webcalls/expenses/extra_expenses_to_delete.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(expense_id)
    else:
        webcall = open('src/db/webcalls/expenses/periodic_expenses_to_delete.sql', mode='r')
        readed_query = webcall.read()
        webcall.close()
        readed_query_2_execute = readed_query.format(expenseid)

    try:
        connection, cursor = dbconnection()
        cursor.execute(readed_query_2_execute)
        connection.commit()
    except Exception as e:
        print(f"Error at filtered month data SQL query: {e}")    
    finally:
        connection.close()
    
    return redirect(url_for('manage_expenses'))

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