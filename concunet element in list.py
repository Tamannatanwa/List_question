a=["man"]
i=0
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        n=a[i][j]
        c.append(n)
        j=j+1
    i=i+1
print(c)