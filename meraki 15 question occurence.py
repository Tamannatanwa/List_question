a=['a','n','t','a','a','t','n','n','a','x','u','g','a','x','a']
i=0
b=[]
while i<len(a):
    if a[i]>="a" and a[i]<="z":
        n=a.count(a[i])
        b.append(n)
        print(a[i],n)
        i=i+1
print(b)

i=0
while i<len(a):
    b=a.count('a')
    n=a.count('n')
    t=a.count('t')
    x=a.count('x')
    u=a.count('u')
    g=a.count('g')
    i=i+1
print("a=",b,"times")
print("n=",n,"times")
print("t=",t,"times")
print("x=",x,"times")
print("u=",u,"times")
print("g=",g,"times")
print("i=",i,"times")
