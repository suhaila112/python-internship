from typing import Optional
import json
import requests
from pydantic import BaseModel, ValidationError
class UserModel(BaseModel):
    name: str
    email: str
    age: int
class TaskModel(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    completed: bool = False
class JokeModel(BaseModel):
    type: str
    setup: str
    punchline: str
    id: int
def create_task(data: dict) -> TaskModel:
    return TaskModel(**data)
def tasks_to_json(tasks: list[TaskModel]) -> str:
    return json.dumps([task.model_dump() for task in tasks], indent=2)
def print_clean_error(error: ValidationError) -> None:
    for err in error.errors():
        field = err["loc"][0]
        message = err["msg"]
        print(f"{field}: {message}")
tasks: list[TaskModel] = []
try:
    user = UserModel(
        name="Amal",
        email="amal@gmail.com",
        age=20
    )
    print("User created successfully:")
    print(user)
except ValidationError as e:
    print_clean_error(e)
print("-" * 40)
try:
    task1 = create_task({
        "title": "Learn Pydantic",
        "description": "Practice BaseModel validation",
        "priority": "high",
        "completed": False
    })
    task2 = create_task({
        "title": "Complete FastAPI task",
        "priority": "medium"
    })
    tasks.append(task1)
    tasks.append(task2)
    print("Tasks created successfully:")
    print(task1)
    print(task2)
except ValidationError as e:
    print_clean_error(e)
print("-" * 40)
try:
    bad_task = create_task({
        "title": 123,
        "description": ["wrong"],
        "priority": 50,
        "completed": "hello"
    })
except ValidationError as e:
    print("Validation Error:")
    print_clean_error(e)
print("-" * 40)
json_data = tasks_to_json(tasks)
print("Tasks JSON:")
print(json_data)
print("-" * 40)
try:
    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke"
    )
    if response.status_code == 200:
        api_data = response.json()
        joke = JokeModel(**api_data)
        print("Joke API Parsed Successfully:")
        print(f"Setup: {joke.setup}")
        print(f"Punchline: {joke.punchline}")
    else:
        print("Failed to fetch API data")
except ValidationError as e:
    print("API Validation Error:")
    print_clean_error(e)
except requests.RequestException as e:
    print(f"API Request Error: {e}")