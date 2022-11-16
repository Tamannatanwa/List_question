a="tamannatanwar"
i=0
b=[]
c=[]
while i<len(a):
    n=a[i]
    if n not in c:
        c.append(n)
        j=0
        while j<len(a):
            count=a.count(n)
            b.append(count)
            b.append(n)
            j=j+1
            break
    i=i+1
print(b)

