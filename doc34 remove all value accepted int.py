a=[34.67,12,-94.89,"python",0,"c#"]
i=0
b=[]
while i<len(a):
    n=a[i]
    if type (n) is int:
        b.append(n)
    i=i+1
print(b)
        