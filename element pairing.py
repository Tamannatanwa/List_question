a=[89,56,71,46]
i=0
c=[]
while i<len(a):
    sum=0
    while a[i]>0:
        r=a[i]%10
        sum+=r
        a[i]=a[i]//10
    c.append(sum)
    i=i+1
print(c)