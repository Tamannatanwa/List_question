
a=[1,2,3,4,[4,5,6,7],8,9,10,11]
i=0
b=[]
while i<len(a):
    if type (a[i]) is list:
        j=0
        while j<len(a[i]):
            c=a[i][j]
            b.append(c)
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)







a=[[1,2,3,4,5],[6,7,8,9,10]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        c=a[i][j]
        b.append(c)
        j=j+1
    i=i+1
print(b)
    