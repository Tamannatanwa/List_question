a=[[0,1,2],
   [2,3,4],
   [3,4,5,6],
   [7,8,9,10,11],
   [12,13,14]]
i=0
while i<len(a):
    j=0
    sum=0
    count=0
    while j<len(a[i]):
        sum+=a[i][j]
        count+=1
        j=j+1
    i=i+1
    ave=sum/count
    print(ave)

