a=[3,5,0,13,0,2]
i=0
b=[]
c=[]
while i<len(a):
    n=a[i]
    if a[i]!=0:
        b.append(n)
    else:
        c.append(n)
    i=i+1
list=b+c
print(list)
