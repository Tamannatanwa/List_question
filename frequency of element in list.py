a=int(input("enter the length:"))
element=int(input("enter the element:"))
i=0
count=0
c=[]
while i<a:
    x=int(input("enter the item:"))
    c.append(x)
    if element==c[i]:
        count+=1
    i=i+1
if count==0:
    print(element,"not found in given list")
else:
    print(element,"has frequency as",count,"in given list")
    