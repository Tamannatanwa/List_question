a=[4,5,5,5,3,8]
k=3
i=0
b=[]
while i<len(a): 
    if i in a:
        n=a.count(i)
        if n==k:
            if b.count(i)==0:
                b.append(i)
    i=i+1
print(b)
            