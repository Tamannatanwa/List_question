a=[[10,20,30],[40,50,60],[70,80,90],[11,22,33],[44,55,66],[12,13,14]]
#a=x[1:5]
i=0
g=[]
while i<len(a):
    n=a[i]
    j=0
    while j<len(n):
        g.append(n[j])
        j=j+1
    i=i+1
print(g)