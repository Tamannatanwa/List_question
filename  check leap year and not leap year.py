a=int(input("enter the number"))
while True:
    if a%4==0:
        b=a-4
        print(a,b,"it is leap year")
        break
    else:
        d=a+4
        print(a,d,"not leap year")
        break