from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3

router = APIRouter()

# =========================
# DATABASE CONNECTION
# =========================
conn = sqlite3.connect("taskmanager.db", check_same_thread=False)
cursor = conn.cursor()


# =========================
# TASK MODEL
# =========================
class TaskCreate(BaseModel):
    username: str
    title: str
    description: str
    priority: str
    due_date: str


# =========================
# CREATE TASK
# =========================
@router.post("/tasks")
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
@router.get("/tasks/{username}")
def get_tasks(username: str):

    cursor.execute(
        "SELECT * FROM tasks WHERE username=?",
        (username,)
    )

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
@router.put("/tasks/{task_id}")
def complete_task(task_id: int):

    cursor.execute("""
        UPDATE tasks
        SET completed=1
        WHERE id=?
    """, (task_id,))

    conn.commit()

    return {"message": "Task completed"}


# =========================
# DELETE TASK
# =========================
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()

    return {"message": "Task deleted"}