marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
]


i=0
sum=0
while i<len(marks):
    num=marks[i]
    j=0
    sum=0
    while j<len(num):
        n=num[j]
        sum=sum+n
        j+=1
    i=i+1
    # ave=sum/len(num)
ave=sum/len(marks)
print(ave)