a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
c=[]
d=[]
while i<len(a):
    if a[i] not in d:
        d.append(a[i])
        b=a.count(a[i])
        c.append(b)
        c.append(a[i])
    i+=1
print(c)