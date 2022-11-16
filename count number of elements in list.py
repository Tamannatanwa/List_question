a=["python","list","exrcise","practice","solution"]
b=[len(i) for i in a]
print(b)

i=0
b=[]
while i<len(a):
    num=a[i]
    re=num[::-1]
    b.append(re)
    i=i+1
print(b)


i=0
c=[]
while i<len(a):
    j=0
    count=0
    while j<len(a[i]):
        count+=1
        j=j+1
    i=i+1
    c.append(count)
print(c)
