a=[[1,2],3,[4],[6,7],8,9]
i=0
sum=0
num=0
while i<len(a):
    if type (a[i]) is list:
        j=0
        while j<len(a[i]):
            n=a[i][j]
            sum+=n
            j=j+1
    else:
        num+=a[i]
    i=i+1
total=sum+num
print(total)