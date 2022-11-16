a=['a','b','c','d','e']
b=['b','e','g','c']
i=0
d=[]
while i<len(a):
    if a[i] not in b:
        d.append(b[i])
    i=i+1
print(d)
        