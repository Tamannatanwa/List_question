a=[[1,2],[3,4]]
i=0
sum=0
while i<len(a):
    j=0
    while j<=i:
        sum+=a[i][j]
        j=j+1
    i=i+1
print(sum)