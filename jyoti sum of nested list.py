a=[[1,2,3],4,5,6]
i=0
sum=0
c=[]
while i<len(a):
    if type (a[i]) is list:
        j=0
        count=0
        while j<len(a[i]):
            count+=a[i][j]
            c.append(a[i][j])
            
            j=j+1
    else:
        sum+=a[i]
        c.append(a[i])
    i=i+1
print(count+sum)
print(c)
