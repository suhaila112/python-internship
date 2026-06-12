from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from database import (
    init_db,
    get_connection
)

from auth import (
    hash_password,
    verify_password,
    create_token,
    get_current_user,
    sessions
)

from schemas import (
    UserCreate,
    TaskCreate
)

app=FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_headers = ["*"]
    
)

@app.post("/auth/register")
def register(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )

    if cursor.fetchone():
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    hashed = hash_password(
        user.password
    )

    cursor.execute(
        """
        INSERT INTO users
        (email, hashed_password)
        VALUES (?,?)
        """,
        (
            user.email,
            hashed
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "user registered"
    }
    
@app.post("/auth/login")
def login(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )

    db_user = cursor.fetchone()
    conn.close()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    if not verify_password(
        user.password,
        db_user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
        
    token = create_token()
    sessions[token] = user.email

    return {
        "token": token
    }

@app.get("/auth/me")
def me(
    current_user=Depends(
        get_current_user
    )
):
    return {
        "email": current_user
    }

@app.post("/tasks")
def create_task(
    task: TaskCreate,
    user=Depends(
        get_current_user
    )
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks
        (title,status,ownner_email)
        VALUES(?,?,?)
        """,
        (
            task.title,
            task.status,
            user
        )
    )
    conn.commit()
    conn.close()

    return {
        "message": "Task created"
    }

@app.get("/tasks")
def get_tasks(
    user=Depends(
        get_current_user
    )
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE owner_email=?
        """,
        (user,)
    )

    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
