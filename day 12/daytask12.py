from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3
app=FastAPI()

def get_connection():
    conn=sqlite3.connect("tasks.db")
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=get_connection()
    conn.execute("""
     create  table if not exists tasks(
                id integer primary key autoincrement,
                title text not null,
                status text not null
         )
    """)
    conn.commit()
    conn.close()

@app.on_event("startup")
def startup():
    init_db()

class TaskCreate(BaseModel):
    title:str
    status:str

class TaskUpdate(BaseModel):
    title:str
    status:str

@app.get("/tasks")
def create_task(task:TaskCreate):
    conn=get_connection()

    cursor=conn.execute(
        "insert into task (title ,status) values (?,?)",
        (task.title,task.status)
    )
    conn.commit()
    task_id=cursor.lastrowid
    conn.close()
    return{
        "id":task_id,
        "title":task.title,
        "status":task.status
    }

@app.get("/tasks")
def get_tasks(status:str=None):
    conn=get_connection()
    if status:
        rows=conn.execute(
            "select * from tasks where status=?",
            (status,)
        ).fetchall()
    else:
        rows=conn.execute(
            "select * from tasks"
        ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.put("/tasks/{task_id}")
def update_task(task_id: int,task:
TaskUpdate):
    conn=get_connection()
    cursor=conn.execute(
        """
        update tasks
        set title=?,status=?
        where id=?
        """,
        task.title,task.status,task_id
    )
    conn.commit()
    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )
    conn.close()
    return {
        "message":"task update successfully"
    }

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    conn=get_connection()
    cursor=conn.execute(
        "delete from tasks where id=?",
        (task_id,)
    )
    conn.commit()
    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )
    conn.close()
    return {
        "message":"task deleted successfully"
    }