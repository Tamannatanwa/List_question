a=["python","list","exrcise","practice","solution"]
i=0
b=[]
while i<len(a):
    num=a[i]
    re=num[::-1]
    b.append(re)
    i=i+1
print(b)
