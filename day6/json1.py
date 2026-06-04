import json
students=[
    {"name":"sara","age":20,"marks":97},
    {"name":"maya","age":21,"marks":79},
    {"name":"amal","age":22,"marks":98},
    {"name":"mariya","age":20,"marks":76},
    {"name":"tom","age":21,"marks":86}
    ]
with open("students.json","w") as file:
    json.dump(students,file,indent=2)
    print("data saved successfully")
with open("students.json","r") as file:
        print(file.read())
    