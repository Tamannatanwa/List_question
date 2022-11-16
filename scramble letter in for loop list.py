a=["python","list","exrcise","practice","solution"]
b=[]
for i in a:
    re=i[::-1]
    b.append(re)
print(b)

i=0
b=[]
while i<len(a):
    j=-1
    while j>=-len(a[i]):
        n=a[i][j]
        print(n,end="")
        j=j-1
    print()
    i=i+1

        
        