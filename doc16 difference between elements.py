# a=[1,2,3,4,5,6,7,8,9,10]
a=[2,4,6,8,8,6]
# a=[2,4,6,8]
c=[]
i=0
while i<len(a)-1:
    num=a[i]
    # n=a[i+1]-a[i]
    n=a[i]-a[i+1]
    c.append(n)
    i=i+1
print(c)
    
