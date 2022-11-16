
    
    
a=[-2,3.0,1,4,5,-6,7,0,-9]
i=0
b=[]
c=[]
d=[]
while i<len(a):
    n=a[i]
    if type (n) is float:
        b.append(n)
    elif n>=0:
        if type (n) ==int:
            c.append(n)
    else:
        d.append(n)
    i=i+1
print(b)
print(c)
print(d)