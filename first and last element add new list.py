a=[1,2,3,4,5,6]
i=0
j=-1
b=[]
while i<len(a)/2:
    n=a[i]
    v=a[j]
    b.append(v)
    b.append(n)
    i=i+1
    j=j-1
print(b)
