student_marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
length=len(student_marks)
index=0
less_than=0
more_than=0
while index<length:
    marks=student_marks[index]
    if marks<50:
        less_than+=1
    else:
        more_than+=1
    index=index+1
print("marks more than 50",more_than)
print("marks less than 50",less_than)