a=[1,2,2,5,8,4,4]
b=[]
i=0
count=0
while i<len(a):
    if a[i] not in b:
        n=a[i]
        count+=1
    i=i+1
print(count)
