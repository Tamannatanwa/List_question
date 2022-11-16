
a=["aniket","priya","tamanna","amrita"]
i=0
c=[]
while i<len(a):
    j=0
    count=0
    while j<len(a[i]):
        count+=1
        j=j+1
    i=i+1
    c.append(count)
print(c)
