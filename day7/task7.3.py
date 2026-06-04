def calculate_grade(name:str,marks: list[int])->str:
    avg:float=sum(marks)/len(marks)
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=60:
        return "D"
    else:
        return "Fail"
    return(f"{name}",grade is "{grade}")
grade=calculate_grade([90,87])
print("grade: ",grade)
