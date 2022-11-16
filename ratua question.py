


i=1
while i<=5:
    j=1
    b=[]
    while j<=5:
        x=int(input("enter the element...."))
        j=j+1
        b.append(x)
    i=i+1
    print(b)

    
    
    
# i=1
# count=0
# sum=0
# while i<=5:
#     j=1
#     while j<=5:
#         sum+=1
#         j=j+1
#     count+=1
#     i=i+1
# ave=count+sum
# print(ave-2)




# n=int(input("enter the number of intern"))
# password=int(input("enter the password"))
# i=1
# day=1
# while i<=n:
#     j=0
#     while i<50:
#         day=day+5000+i
#         j=j+1
#     i=i+1
#     day+=1
#     print(day)
    
    
    
a=[1,2,3,4,5,6,7,8,9]
i=0
d=[]
while i<len(a):
    if a[i]%2==0:
        n=a[i]*a[i]
        d.append(n)
    else:
        v=a[i]
        d.append(v)
    i=i+1
print(d)