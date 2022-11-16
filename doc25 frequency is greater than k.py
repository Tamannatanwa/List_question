a=[4,6,4,3,3,4,3,4,3,8]
b=[]
k=3
for i in a:
    n=a.count(i)
    if n>k:
        if b.count(i)==0:
            b.append(i)
print(b)



a=[1,1,1,64,23,64,22,22,22]
i=0
b=[]
c=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        n=a.count(a[i])
        if n>3:
            c.append(a[i])
    i=i+1
print(c)