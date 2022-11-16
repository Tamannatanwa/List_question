a=[9,-8,100,-12,-13]
i=0
b=[]
c=[]
while i<len(a):
    num=a[i]
    if num>0:
        #print(num,"it is positive")
        b.append(num)
    elif num<0:
        #print(num,"it is negative")
        c.append(num)
    else:
        print(num,"it is zero")
    i=i+1
print(b)
print(c)