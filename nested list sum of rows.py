a=[[1,2],[3,4,5],[6,7,8]]
i=0
c=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        n=a[i][j]
        sum+=n
        j=j+1
    c.append(sum)
    i=i+1
print(c)
i=0
sum=0
while i<len(c):
    sum+=c[i]
    i=i+1
print(sum)