a=[6,1,3,5,6,3,1]
b=[]
i=0
index=0
pro=1
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        n=b[index]
        pro=pro*n
        index+=1
    i=i+1
print(b)
print(pro)

