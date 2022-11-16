a=[12,23,12]
length=len(a)
element=int(input("enter the element"))
count=0
for i in range(0,length):
    if element==a[i]:
        count+=1
if count==0:
    print(element,"not found in given list")
else:
    print(element,"has frequency as",count,"in given list")
    
    
