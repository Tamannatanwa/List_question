a=[[2,3,4,5],[5,6,7],[[3,4,8],0,12]]
i=0
b=[]
while i<len(a):
    n=a[i]
    j=0
    while j<len(n):
        b.append(n[j])
        j=j+1
    i=i+1
i=0
d=[]
while i<len(b):
    if type (b[i]) is list:
            j=0
            while j<len(b[i]):
                c=b[i][j]
                d.append(c)
                j+=1
            i=i+1
    else:
        d.append(b[i])
        i=i+1
print(d)


