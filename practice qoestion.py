# a=[1,2,3]
# a.extend([3,2])
# print(a)

a=[1,2,3,4,5,6]
i=0
c=a[::-1]
b=[]
while i<len(a)/2:
    b.append(c[i])
    b.append(a[i])
    i+=1
print(b)

