a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
i=0
b=[]
while i<len(a):
    n=a[i],a[i+1],a[i+2]
    b.append(list(n))
    i=i+3
print(b)
    