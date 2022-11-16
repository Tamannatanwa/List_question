
a=int(input("enter the length....."))
b=[]
i=0
max=0 
secondmax=0
thirdmax=0
while i<a:
    x=int(input("enter number...."))
    b.append(x)
    if b[i]>max:
       thirdmax=secondmax
       secondmax=max
       max=b[i]
    elif b[i]>secondmax:
        thirdmax=secondmax
        secondmax=b[i]
    elif b[i]>thirdmax:
        thirdmax=b[i]
    i=i+1
print("the first max:",max)
print("the second max:",secondmax)
print("the third max:",thirdmax)
        
        
    

