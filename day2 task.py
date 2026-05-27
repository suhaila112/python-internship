marks=[10,20,30,40,50,60,70,80,90,100]
total=sum(marks)
print("total marks:",total)
average=sum(marks)/len(marks)
print("average marks:",average)
highest=max(marks)
print("highest marks:",highest)
smallest=min(marks)
print("smallest marks:",smallest)
unique=list(set(marks))
print("unique marks:",unique)
above=[]
for i in marks:
    if i>average:
        above.append(i)
print("above marks:",above)


