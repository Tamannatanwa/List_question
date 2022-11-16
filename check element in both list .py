a=[1,2,3,4,5,6]
b=[2,3,1,0,6,7]
c=[]
for i in a:
    for j in b:
        if i not in b:
            c.append(i)
        break
print(c)