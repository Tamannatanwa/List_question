a=[7,8,4,5,6,2,1]
i=0
count=0
while i<len(a):
    n=a[i]
    if i%2==0:
        count+=n
    i=i+1
print(count)

    