import sqlite3
import Table_create

def connect():
    try:
        connection = sqlite3.connect("password_manager.db")
        return connection
    except (Exception, sqlite3.Error) as error:
        print(error)

def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        sqlite_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (?, ?, ?, ?, ?)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(sqlite_insert_query, record_to_insert)
        connection.commit()
    except (Exception, sqlite3.Error) as error:
        print(error)

def find_password(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        sqlite_select_query = """SELECT password FROM accounts WHERE app_name=(?)"""
        cursor.execute(sqlite_select_query, [app_name])
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ')
        print(result[0])
        print('')
        print('-' * 30)
    except (Exception, sqlite3.Error) as error:
        print(error)

def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
    try:
        connection = connect()
        cursor = connection.cursor()
        sqlite_select_query = ('SELECT * FROM accounts WHERE email=?')
        cursor.execute(sqlite_select_query, [user_email])
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row)):
                print(data[i] + row[i])
        print('')
        print('-' * 30)
    except (Exception, sqlite3.Error) as error:
        print(error)
