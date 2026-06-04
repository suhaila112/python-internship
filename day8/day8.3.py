from pydantic import BaseModel,ValidationError 
class TaskModel(BaseModel):
    title:str
    priority:str="low"
    completed:bool=False
try:
    task=TaskModel(
    title="complete fastapi task",
    priority="high",
    completed=True
) 
    print("valid task created")
except ValidationError as e:
    print(e)
print("\n" + "e" * 40 + "\n")
try:
 bad_task=TaskModel(
    title=123,
    priority=['high'],
    completed="hello"
)
except ValidationError as e:
    print("validation error: ")
    print("-"*30)
    for error in e.errors():
      field=error["loc"][0]
      message=error['msg']
      print(f"{field}: {message}")