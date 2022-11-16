a=int(input("enter thhe length....."))
b=[]
i=0
while i<a:
    x=int(input("enter the element"))
    b.append(x)
    n=b[i]
    r=n*1
    m=n%100
    c=n%10
    i=i+1
print(r-m,'+',m-c,"+",c)