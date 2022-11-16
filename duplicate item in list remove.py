a=[10,20,30,30,40,50,50,60,70]
i=0
b=[]
pro=1
while i<len(a):
    if a[i]not in b:
        b.append(a[i])
    i=i+1
print(b)       