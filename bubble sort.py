
a=int(input("enter the length......"))
i=0
b=[]
while i<a:
    x=int(input("enter the element"))
    b.append(x)
    i=i+1
k=0
while k<a:
    j=0
    while j<(a-k-1):
        if b[j]>b[j+1]:
            c=b[j]
            b[j]=b[j+1]
            b[j+1]=c
        j=j+1
    k=k+1
print("bubble sort")
print(b)

    
        
        
        


