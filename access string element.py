a=['a','b','c','d']
b=['b','e','e','c']
i=0
c=[]
while i<len(a):
    n=a[i+1]
    f=a[i+2]
    c.append(n)
    c.extend(f)
    i=i+1
    break
print(c)
    


    