a=[]
b=[]
n=int(input("enter the total number inside list:"))
i=1
while (i<=n):
    num=int(input("enter the element in the list:"))
    i=i+1
    a.append(num)
print(a,"the given list by you is here.\n")


a.sort()
print(a)
print(max(a))

