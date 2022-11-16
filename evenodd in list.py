a=[50,40,23,70,56,12,5,10,7]
index=0
while index<len(a):
    num=a[index]
    if num%2==0:
        print(num,"even number")
    else:
        print(num,"odd number")
    index+=1
