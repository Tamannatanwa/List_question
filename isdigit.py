a=[10,10,10,20,30,50,60,20,50,10]
i=0
c=[]
v=[]
while i<len(a)/2:
    j=0
    b=[]
    while j<len(a):
        if a[i] not in v:
            v.append(a[i])
        if a[i]==a[j]:
            b.append(a[i])
            b.append(a[j])
            break
        j=j+1
    i=i+1
    c.append(b)
print(c)



a=[10,10,10,20,30,50,60,20,50,10]
i=0
v=[]
while i<len(a):
    if a[i] not in v:
        v.append(a[i])
j=0
while j<len(v):
    c=0
    while c<len(a):
        
    
        