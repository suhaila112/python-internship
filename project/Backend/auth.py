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
# USER MODELS
# =========================
class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# =========================
# REGISTER USER
# =========================
@router.post("/register")
def register(user: UserRegister):

    cursor.execute("SELECT * FROM users WHERE username=?", (user.username,))
    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    cursor.execute("""
        INSERT INTO users(username, email, password)
        VALUES(?,?,?)
    """, (user.username, user.email, user.password))

    conn.commit()

    return {"message": "User registered successfully"}


# =========================
# LOGIN USER
# =========================
@router.post("/login")
def login(user: UserLogin):

    cursor.execute("""
        SELECT * FROM users
        WHERE username=? AND password=?
    """, (user.username, user.password))

    db_user = cursor.fetchone()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "username": user.username
    }