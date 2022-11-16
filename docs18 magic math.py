a=[6,2,3,8]
a.sort()
index=0
count=0
i=a[index]

while i<=8:
    n=a[index]
    if n==i:
        index+=1
    else:
        print(i)
        count+=1
    i=i+1
print()
print(count)






