a=[[1,3],[0],[9,11],[13,15,17]]
i=0
max=0
min=10
while i<len(a):
    c=len(a[i])
    if c>max:
        max=c
        e=a[i]
    elif c<min:
        min=c
        f=a[i]
    i=i+1
print("list maximum is","(",max,",",e,")")
print("list minimum is","(",min,",",f,")")