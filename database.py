# Create and manage the sqlite database
# Autor: Toni Dahlitz
# Datum: 2025-02-07
# Version: 0.1

import sqlite3
from sqlite3 import Error


# Verbindung zur SQLite-Datenbank (oder Erstellen einer neuen, wenn sie nicht existiert)
def create_connection():
    return sqlite3.connect('pku_control.db')
        
# Erstellen einer Tabelle (falls noch nicht vorhanden)
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

# Einfügen von Daten in die Tabelle
def insert_data(date, phe_value, tyr_value, comment):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO werte (date, phe_value, tyr_value, comment)
    VALUES (?, ?, ?, ?)
    ''', (date, phe_value, tyr_value, comment))
    connection.commit()
    connection.close()

def show_data():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT phe_value, tyr_value, date, comment FROM werte ORDER BY date DESC')
    data = cursor.fetchall()
    return data

create_table()