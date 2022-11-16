a=["jyoti","tamanna","ashwini"]
i=0
j=-1
b=[]
count=0
while i<len(a):
    if count==2:
         b.append(a[2][0])
    if count==i:
        d=a[i][j]
        b.append(d)
    i=i+1
    count+=1
print(b)