
n=[10,11,12,13,14,17,18,19]
# n=[20,5,10,23,25,7]
i=0
a=[]
number=30
while i<len(n):
    j=0
    b=[]
    while j<len(n):
        if n[i]+n[j]==number and n[j]>n[i]:
            b.append(n[i])
            b.append(n[j])
            a.append(b)
        j+=1
    i+=1
print(a)