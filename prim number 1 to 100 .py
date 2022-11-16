a=list(range(100,200))
i=0
b=[]
while a[i]<a[-1]:
    count=0
    j=1
    while j<=a[i]:
        if a[i]%j==0:
            count+=1
        j=j+1
    if count==2:
        b.append(a[i])
    a[i]+=1
    i=i+1
print(b)

    
        
        
        