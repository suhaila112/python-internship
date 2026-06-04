def greet(name):
    return f"Hello {name}"
def calculate_grade(marks):
    if marks>90:
        return "A"
    elif marks>80:
        return "B" 
    elif marks>65:
        return "C" 
    elif marks>45:
        return "D" 
    else:
        return "F"
name=input("enter your name: ")
marks=int(input("enter marks: "))
print(greet(name))
grade= calculate_grade(marks)
print(f"name: {name}")
print(f"marks: {marks}")
print(f"grade: {grade}")

    