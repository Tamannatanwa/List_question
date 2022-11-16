a=["rajitha"]
i=0
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if j!=1 and j!=2 and j<=5:
            c.append(j)
        j=j+1
    i=i+1
print(c)