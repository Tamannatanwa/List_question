l=[4, 5, 5, 5, 3, 8]
i=0
b=[]
c=[]
while i<len(l):
    d=l[i]
    if d not in b:
        b.append(d)
        n=l.count(d)
        if n==3:
            c.append(d)
    i=i+1
print(c)