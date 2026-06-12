import sqlite3
def  get_connection():
    return sqlite3.connect("task.db")
def init_db():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY
    AUTOINCREMENT,
                   email TEXT UNIQUE,
                   hashed_password TEXT
    )
    """)