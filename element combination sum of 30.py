a=[13,2,15,18,15,92,28,16,12]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a):
        if a[i] + a[j]==30:
            c=[a[i],a[j]]
            b.append(c)
        j=j+1
    i=i+1
print(b)
    

