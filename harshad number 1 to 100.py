for i in range(1,101):
    a=i
    sum=0
    while i>0:
        digit=i%10
        sum=sum+digit
        i=i//10
    if a%sum==0:
        print(a, end=",")
        






