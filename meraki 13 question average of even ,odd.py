a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
se=0
count=0
co=0
while i<len(a):
    n=a[i]
    if n%2==0:
        count+=1
        sum+=n
    else:
        se+=n
        co+=1
    i+=1
ave=sum/count
average=se/co
print("average of even number=",ave)
print("average of odd number=",average)