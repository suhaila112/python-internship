import sqlite3

# =========================
# CONNECT DATABASE
# =========================
conn = sqlite3.connect("taskmanager.db", check_same_thread=False)
cursor = conn.cursor()


# =========================
# CREATE USERS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")


# =========================
# CREATE TASKS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT,
    due_date TEXT,
    completed INTEGER DEFAULT 0
)
""")


# =========================
# SAVE CHANGES
# =========================
conn.commit()
conn.close()
