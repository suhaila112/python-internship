from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=201
)
def create_task(task: TaskCreate):

    new_task = {
        "id": 1,
        "title": task.title,
        "completed": task.completed
    }

    return new_task