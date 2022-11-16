
a=["aniket","tamanna","priya","amrita"]
i=0
b=[]
while i<len(a):
    num=a[i]
    re=num[::-1]
    b.append(re)
    i=i+1
print(b)
