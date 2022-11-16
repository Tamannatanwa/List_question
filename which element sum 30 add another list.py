a=[15,7,23,15,8,12,9,18]
n=30
i=0
c=[]
count=0
while i<len(a):
    j=0
    b=[]
    while j<len(a):
        if a[i]+a[j]==n and a[j]>a[i]: 
            b.append(a[i])
            b.append(a[j])
            c.append(b)
        elif count==0:
            if a[i]+a[j]==n and a[i]==a[j]:
                b.append(a[i])
                b.append(a[j])
                c.append(b)
                break
        j=j+1
    i=i+1
    count+=1
print(c)




