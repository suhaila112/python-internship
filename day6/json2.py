import json
with open("students.json", "r") as file:
    students=json.load(file)
for student in students:
    print(f"name:{student['name']}, age:{student['age']}, marks:{student['marks']}")
    