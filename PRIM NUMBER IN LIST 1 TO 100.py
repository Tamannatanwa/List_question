


a=int(input("enter the no."))
b=int(input("enter the no."))
while a<=b:
    fac=0
    i=1
    while i<=a:
        if a%i==0:
            fac=fac+1
        i=i+1
    if fac==2:
        print(a)
    a+=1
    
    
    
