a=[[1,2,1],[4,5,6],[10,3]]
i=0
d=[]
num=0
while i<len(a):
    n=a[i]
    j=0
    sum=0
    while j<len(n):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
    num=num+sum
d.append(num)
print(d)