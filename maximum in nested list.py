a=[ [1,3],[0],[5,7],[9,11],[8,15,17]]
i=0
max=0
min=a[i]
while i<len(a):
    b=a[i]
    c=len(b)
    if c>max:
        max=c
        b=a[i]
    else:
        min=c
        d=a[i]
    i=i+1
print("list lenth maximum","(",max,",",b,")")
print("list lenth minimum","(",min,",",d,")")





a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=0
min=a[i]
while i<len(a):
    b=a[i]
    c=len(b)
    if c>max:
        max=c
        b=a[i]
    elif a[i]<min:
        min=a[i]
    i=i+1
j=max,b
e=min
print(e)
print(j)



