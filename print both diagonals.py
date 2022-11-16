a=[[1,2,3],
   [4,5,6],
   [7,8,10]]
i=0
index=0
sum=0
while i<len(a):
    j=2
    while j<len(a[i]):
        sum+=a[i][index]
        j=j+1
        index+=1
    i+=1
i=0
index=2
count=0
while i<len(a):
    j=2
    while j<len(a[i]):
        count+=a[i][index]
        j=j+1
        index-=1
    i+=1
ave=sum-count
print(ave)