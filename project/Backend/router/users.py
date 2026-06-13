from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter()

# =========================
# DATABASE CONNECTION
# =========================
conn = sqlite3.connect("taskmanager.db", check_same_thread=False)
cursor = conn.cursor()


# =========================
# GET ALL USERS
# =========================
@router.get("/users")
def get_all_users():

    cursor.execute("SELECT id, username, email FROM users")
    rows = cursor.fetchall()

    users = []

    for row in rows:
        users.append({
            "id": row[0],
            "username": row[1],
            "email": row[2]
        })

    return users


# =========================
# GET SINGLE USER
# =========================
@router.get("/users/{username}")
def get_user(username: str):

    cursor.execute(
        "SELECT id, username, email FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user[0],
        "username": user[1],
        "email": user[2]
    }


# =========================
# DELETE USER
# =========================
@router.delete("/users/{username}")
def delete_user(username: str):

    cursor.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()

    return {"message": "User deleted"}