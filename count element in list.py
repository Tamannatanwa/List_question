a=["tamannatanwar"]
i=0
d=[]
b=[]
while i<len(a):
    n=a[i]
    j=0
    while j<12:
        f=a.count(a[i][j])
        num=a[i][j]
        if num not in b:
            b.append(num)
            f=a.count(a[i][j])
            d.append(f)
            d.append(num)
        j=j+1
    i=i+1
print(d)