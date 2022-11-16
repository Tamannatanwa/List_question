a=[1,2,3,4,5,6,7,8,9]
i=0
d=[]
while i<len(a):
    if a[i]%2==0:
        n=a[i]*a[i]
        d.append(n)
    else:
        v=a[i]
        d.append(v)
    i=i+1
print(d)