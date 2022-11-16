a=["hello","take"]
b=["dear","sir"]
i=0
c=[]
while i<len(a):
    j=0
    while j<len(b):
        n=a[i],b[j]
        c.append(list(n))
        j=j+1
    i=i+1
print(c)