a=[10,10,10,20,30,50,60,20,50,10]
i=0
b=[]
c=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        n=a.count(a[i])
        if j==10:
            c.append(a[i])
            j=j+1
    i=i+1
print(c)