from pydantic import BaseModel


# =========================
# USER SCHEMAS
# =========================
class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# =========================
# TASK SCHEMAS
# =========================
class TaskCreate(BaseModel):
    username: str
    title: str
    description: str
    priority: str
    due_date: str


class TaskOut(BaseModel):
    id: int
    username: str
    title: str
    description: str
    priority: str
    due_date: str
    completed: bool