a=int(input("enter the length:-"))
b=[]
i=0
while i<a:
    x=int(input("enter the number="))
    b.append(x)
    num=b[i]
    n=num*1
    r=num%1000
    m=r%100
    y=m%10
    i=i+1
    print('"',n-r,"+",r-m,"+",m-y,"+",y,'"')
    
