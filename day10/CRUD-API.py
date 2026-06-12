from fastapi import FastAPI,HTTPException, status
from pydantic import BaseModel
app = FastAPI()
tasks = {}
next_id = 1
class taskcreate(BaseModel):
    title: str
class taskupdate(BaseModel):
    title: str | None = None
    completed: bool | None = None
class taskresponse(BaseModel):
    id: int
    title: str
    completed: bool

@app.get("/tasks",
response_model=list[taskresponse])
def get_all_tasks():
    return list(tasks.values())
@app.get("/tasks/{task_id}",
response_model=taskresponse)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404, 
            detail="task not found"
        )
    return tasks[task_id]

@app.post("/tasks", response_model=taskresponse, status_code=status.HTTP_201_CREATED)
def create_task(task: taskcreate):
    global next_id
    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": False
    }
    tasks[next_id] = new_task
    next_id += 1
    return new_task
@app.put("/tasks/{task_id}", response_model=taskresponse)
def update_task(task_id: int, task: taskcreate):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
detail="task not found")
    tasks[task_id]  = {
        "id": task_id,
        "title": task.title,
        "completed": tasks[task_id]["completed"]
       }
    return tasks[task_id]
@app.delete("/tasks/{task_id")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
detail="task not found")
    
    del tasks[task_id]
    return {"message": "task deleted successfully"}

@app.patch("/tasks/{task_id}/complete",
response_model=taskresponse)
def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
detail="task not found")
    tasks[task_id]["completed"] = True
    return tasks[task_id]