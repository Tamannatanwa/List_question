a=[-2,3.1,4,5,-6,7.0,-9]
i=0
t=[]
f=[]
n=[]
while i<len(a):
    if type (a[i])==int and a[i]>0:
        t.append(a[i])
    elif (type(a[i]))==float:
        f.append(a[i])
    elif type (a[i])==int and a[i]<0:
        n.append(a[i])
    i=i+1
print(t)
print(f)
print(n)