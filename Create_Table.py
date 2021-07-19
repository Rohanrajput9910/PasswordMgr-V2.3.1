import sqlite3

conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS accounts (
                       password text,
                        email text,
                        username text,
                        url text,
                        app_name text
                        )
""")
conn.commit()
conn.close()
