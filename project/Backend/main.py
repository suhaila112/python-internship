from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# =========================
# DATABASE CONNECTION
# =========================
conn = sqlite3.connect("taskmanager.db", check_same_thread=False)
cursor = conn.cursor()


# =========================
# TABLE CREATION
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    title TEXT,
    description TEXT,
    priority TEXT,
    due_date TEXT,
    completed INTEGER DEFAULT 0
)
""")

conn.commit()


# =========================
# MODELS
# =========================
class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class TaskCreate(BaseModel):
    username: str
    title: str
    description: str
    priority: str
    due_date: str


# =========================
# REGISTER
# =========================
@app.post("/register")
def register(user: UserRegister):

    cursor.execute("SELECT * FROM users WHERE username=?", (user.username,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="Username already exists")

    cursor.execute("""
        INSERT INTO users(username, email, password)
        VALUES(?,?,?)
    """, (user.username, user.email, user.password))

    conn.commit()

    return {"message": "Registration successful"}


# =========================
# LOGIN
# =========================
@app.post("/login")
def login(user: UserLogin):

    cursor.execute("""
        SELECT * FROM users
        WHERE username=? AND password=?
    """, (user.username, user.password))

    db_user = cursor.fetchone()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "username": user.username}


# =========================
# CREATE TASK
# =========================
@app.post("/tasks")
def create_task(task: TaskCreate):

    cursor.execute("""
        INSERT INTO tasks(username, title, description, priority, due_date, completed)
        VALUES(?,?,?,?,?,0)
    """, (
        task.username,
        task.title,
        task.description,
        task.priority,
        task.due_date
    ))

    conn.commit()

    return {"message": "Task created"}


# =========================
# GET ALL TASKS
# =========================
@app.get("/tasks/{username}")
def get_tasks(username: str):

    cursor.execute("SELECT * FROM tasks WHERE username=?", (username,))
    rows = cursor.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "username": row[1],
            "title": row[2],
            "description": row[3],
            "priority": row[4],
            "due_date": row[5],
            "completed": bool(row[6])
        })

    return tasks


# =========================
# COMPLETE TASK
# =========================
@app.put("/tasks/{task_id}")
def complete_task(task_id: int):

    cursor.execute("""
        UPDATE tasks
        SET completed=1
        WHERE id=?
    """, (task_id,))

    conn.commit()

    return {"message": "Task marked as completed"}


# =========================
# DELETE TASK
# =========================
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

    return {"message": "Task deleted"}