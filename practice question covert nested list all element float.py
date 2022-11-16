a=[[1,2,3],[4,5,6,],[7],[8,9]]
i=0
b=[]
d=[]
while i<len(a):
    c=a[i]
    j=0
    while j<len(c):
        b.append(c[j])
        d.append(float(c[j]))
        j=j+1
    i=i+1
print(b)
print(d)