a=[[0],[1,3],[9,11],[13,15,17]]
i=0
min=10
max=0
while i<len(a):
    n=len(a[i])
    if n>max:
        max=n
        r=a[i]
    if n<min:
        min=n
        h=a[i]
    i=i+1
k=max,r
v=min,h
print(tuple(k))
print(tuple(v))