a=[12,3,6,8,9,10,11,13,15]
i=0
b=[]
while i<len(a):
    if a[i]%2!=0:
        b.append(a[i])
    i=i+1
print(b)