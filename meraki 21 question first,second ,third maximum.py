a=int(input("enter the length"))
i=0
b=[]
while i<(a):
    user=int(input("enter the number"))
    b.append(user)
    i=i+1
b.sort()
print(b[-1],"first maximum")
print(b[-2],"second maximum")
print(b[-3],"third maximum")

