a=[2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
k=3
i=0
count=0
while i<len(a):
    count+=1
    i=i+1
count=count-k
j=0
c=[]
while j<count:
    n=a[j]
    c.append(n)
    j=j+1
print(c)
    
    
    
