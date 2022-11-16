


a=int(input("enter the year"))
while a>0:
    if a%4==0:
        b=a-4
        e=b-4
        print("it is leap year=",a,b,e)
        break
    else:
        c=a+4
        d=c+4
        print("not leap year",a,c,d)
        break


a=[1.2,3,7]