a=[
    [78,76,94,86,88],
    [91,71,98,65],
    [95,45,78],
    [87,67,49,68,88],
]
i=0
while i<len(a):
    num=a[i]
    j=0
    sum=0
    while j<len(num):
        n=num[j]
        sum+=n
        j=j+1
    ave=sum/len(num)
    print(ave)
    i=i+1