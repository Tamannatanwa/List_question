






a=[1,1,2,3,4,4,5,1]
i=0
c=[]
b=[]
while i<len(a)-1:
    j=0
    count=0
    while j<len(a):
        if a[i] not in b:
            b.append(a[i])
            if a[i]==a[i+1]:
                n=count+a[i]-i
                count=n+a[j]
                c.append(count)
                c.append(a[i])
            else:
                c.append(a[i])
        j=j+1
    i=i+1
print(c)
