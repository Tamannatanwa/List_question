a="rajitha is singing loudly"
i=0
b=a.split()
c=[]
while i<len(b):
    if b[i]!="singing":
        c.append(b[i])
    i=i+1
print(c)
        