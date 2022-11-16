a=[1,2,3,4,5,6]
b=a[-1::-1]
i=0
c=[]
while i<len(a)/2:
    c.append(b[i])
    c.append(a[i])
    i=i+1
print(c)
    