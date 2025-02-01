import re
from flask import Flask, request, jsonify, render_template
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Function to execute SQL queries
def execute_sql_query(query, params=()):
    connection = sqlite3.connect('company.db')
    cursor = connection.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    connection.close()
    return results

# Function to check if the DB connection is successful
def check_db_connection():
    try:
        connection = sqlite3.connect('company.db')
        connection.close()
        return True
    except sqlite3.Error as e:
        return False

# Function to get employees in a department
def get_employees_in_department(department):
    query = "SELECT Name FROM Employees WHERE Department = ?"
    results = execute_sql_query(query, (department,))
    if results:
        return [r[0] for r in results]
    return f"No employees found in {department} department."

# Function to get manager of a department
def get_manager_of_department(department):
    query = "SELECT Manager FROM Departments WHERE Name = ?"
    results = execute_sql_query(query, (department,))
    if results:
        return results[0][0]
    return f"No department named {department} found."

# Function to get employees hired after a date
def get_employees_hired_after(date):
    query = "SELECT Name FROM Employees WHERE Hire_Date > ?"
    results = execute_sql_query(query, (date,))
    if results:
        return [r[0] for r in results]
    return f"No employees hired after {date}."

# Function to get total salary expense in a department
def get_total_salary_expense(department):
    query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
    results = execute_sql_query(query, (department,))
    if results and results[0][0] is not None:
        return f"Total salary expense for {department} is {results[0][0]}"
    return f"No employees found in {department} department."

# Function to get average salary in a department
def get_average_salary(department):
    query = "SELECT AVG(Salary) FROM Employees WHERE Department = ?"
    results = execute_sql_query(query, (department,))
    if results and results[0][0] is not None:
        return f"Average salary in {department} is {results[0][0]}"
    return f"No employees found in {department} department."

# Function to get the highest salary in a department
def get_highest_salary(department):
    query = "SELECT MAX(Salary) FROM Employees WHERE Department = ?"
    results = execute_sql_query(query, (department,))
    if results and results[0][0] is not None:
        return f"The highest salary in {department} is {results[0][0]}"
    return f"No employees found in {department} department."

# Function to get the lowest salary in a department
def get_lowest_salary(department):
    query = "SELECT MIN(Salary) FROM Employees WHERE Department = ?"
    results = execute_sql_query(query, (department,))
    if results and results[0][0] is not None:
        return f"The lowest salary in {department} is {results[0][0]}"
    return f"No employees found in {department} department."

# Function to get the number of employees in a department
def get_number_of_employees(department):
    query = "SELECT COUNT(*) FROM Employees WHERE Department = ?"
    results = execute_sql_query(query, (department,))
    if results:
        return f"There are {results[0][0]} employees in {department}."
    return f"No employees found in {department} department."

# Function to list all employees
def list_all_employees():
    query = "SELECT Name FROM Employees"
    results = execute_sql_query(query)
    if results:
        return [r[0] for r in results]
    return "No employees found."

# Function to get details of a specific employee
def get_employee_details(name):
    query = "SELECT * FROM Employees WHERE Name = ?"
    results = execute_sql_query(query, (name,))
    if results:
        return results[0]
    return f"No employee named {name} found."

# Function to list all departments
def list_all_departments():
    query = "SELECT Name FROM Departments"
    results = execute_sql_query(query)
    if results:
        return [r[0] for r in results]
    return "No departments found."

# Function to get details of a department
def get_department_details(department):
    query = "SELECT * FROM Departments WHERE Name = ?"
    results = execute_sql_query(query, (department,))
    if results:
        return results[0]
    return f"No department named {department} found."

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to check DB connection
@app.route('/check_db', methods=['GET'])
def check_db():
    if check_db_connection():
        return jsonify({"message": "Database connection successful!"})
    else:
        return jsonify({"message": "Error connecting to the database!"}), 500

# Handle user queries
@app.route('/ask')
def ask():
    query = request.args.get('query', '').lower()

    # Handle different types of queries based on the pattern in the question
    if 'employees in the' in query:
        department_match = re.search(r'in the ([\w\s]+) department', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_employees_in_department(department)
        else:
            response = "Please specify a department."

    elif 'manager of the' in query:
        department_match = re.search(r'of the ([\w\s]+) department', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_manager_of_department(department)
        else:
            response = "Please specify a department."

    elif 'hired after' in query:
        date_match = re.search(r'after (\d{4}-\d{2}-\d{2})', query)
        if date_match:
            date = date_match.group(1).strip()
            response = get_employees_hired_after(date)
        else:
            response = "Please provide a valid date."

    elif 'total salary expense for' in query:
        department_match = re.search(r'for the ([\w\s]+) department', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_total_salary_expense(department)
        else:
            response = "Please specify a department."

    elif 'average salary in the' in query:
        department_match = re.search(r'in the ([\w\s]+) department', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_average_salary(department)
        else:
            response = "Please specify a department."

    elif 'highest salary in the' in query:
        department_match = re.search(r'in the ([\w\s]+) department', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_highest_salary(department)
        else:
            response = "Please specify a department."

    elif 'lowest salary in the' in query:
        department_match = re.search(r'in the ([\w\s]+) department', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_lowest_salary(department)
        else:
            response = "Please specify a department."

    elif 'how many employees are there in the' in query:
        department_match = re.search(r'in the ([\w\s]+) department', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_number_of_employees(department)
        else:
            response = "Please specify a department."

    elif 'list all employees' in query:
        response = list_all_employees()

    elif 'details of employee' in query:
        name_match = re.search(r'details of employee (\w+)', query)
        if name_match:
            name = name_match.group(1).strip()
            response = get_employee_details(name)
        else:
            response = "Please specify an employee."

    elif 'list all departments' in query:
        response = list_all_departments()

    elif 'details of department' in query:
        department_match = re.search(r'details of department ([\w\s]+)', query)
        if department_match:
            department = department_match.group(1).strip()
            response = get_department_details(department)
        else:
            response = "Please specify a department."

    else:
        response = "Sorry, I didn't understand your query."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
