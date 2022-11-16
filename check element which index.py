a=[2,3,4,5,6,7,8]
b=int(input("enter the number"))
count=0
i=0
while i<len(a):
    if b==a[i]:
        print(count,b)
    else:
        print("not in list")
    i=i+1
    count+=1