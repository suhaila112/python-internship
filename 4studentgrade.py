
def calculate_grade(name,*marks):
    print("name:",name)
calculate_grade("abin")
marks=(50,57,48,68,78)
for mark in marks:
    if mark<0:
       print("invalid")
if mark>100:
    print("invalid") 
else:
    print("valid")
total=sum(marks)
count=len(marks)
average=total/count
print("average:",average)
if average>90:
    print("grade=A")
elif average>75:
    print("grade+B")
elif average>50:
    print("grade=C")
else:
    print("grade=F")




