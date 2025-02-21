# Create and manage the sqlite database
# Autor: Toni Dahlitz
# Datum: 2025-02-21
# Version: 0.1

import sqlite3
from sqlite3 import Error

# Create a connection to the database and create database if not exists
def create_connection():
    return sqlite3.connect('database/pku_control.db')
        
# Create a table in the database
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS werte (
        id INTEGER PRIMARY KEY,
        date DATE,
        phe_value FLOAT,
        tyr_value FLOAT,
        comment TEXT
    )
''')
    connection.commit()
    connection.close()
    print('Table created')

# Insert Data into the database
def insert_data(date, phe_value, tyr_value, comment):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO werte (date, phe_value, tyr_value, comment)
    VALUES (?, ?, ?, ?)
    ''', (date, phe_value, tyr_value, comment))
    connection.commit()
    connection.close()
# Show Data
def show_data():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT phe_value, tyr_value, date, comment FROM werte ORDER BY date DESC')
    data = cursor.fetchall()
    return data

create_table()