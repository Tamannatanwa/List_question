a1=[[0,1,2,],[2, 3, 4,],[3, 4, 5, 6,],[7, 8, 9, 10, 11], [12, 13, 14,]]
a=[[0,1,2,0,0], [2,3,4,0,0], [3,4,5,6,0],[7,8,9,10,11], [12,13,14,0,0]]
i=0
c=[]
# i=0
while i<len(a):
    j=0
    sum=0
    k=0
    v=0
    while j<5:
        b=a[j][i]                   
        sum=sum+b
        if b>0:
            k=k+1
        else:
            v+=1
        j=j+1
    s=k+v
    avg=sum/s
    c.append(avg)
    i=i+1
print(c)
