import sqlite3

#connection
conn = sqlite3.connect("task_manager.db",
check_same_thread=False)
cursor = conn.cursor()

#create tables

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL
)
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL
)
""")
    
    conn.commit()
                   