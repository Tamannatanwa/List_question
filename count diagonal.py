a=[[2,1,1],
   [1,1,1],
   [1,1,1]]
i=0
index=0
count=0
while i<len(a):
    j=2
    while j<len(a):
        count+=a[i][index]
        j=j+2
        index+=1
    i=i+1
print(count)