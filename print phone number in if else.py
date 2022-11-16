a=input("enter the number")
b=int(a[0:3])
c=int(a[3:6])
d=int(a[6:10])
if len(a)==10:
    if b>=0 and b<=999:
        if c>=0 and c<=10000:
            if d>=0 and d<=100000:
                print("("+str(b)+")"+"-"+str(c)+"-"+str(d))
            else:
                print("nothing")
        else:
            print("nothing1")
else:
    print("nothing3")
    
    
    
                                                                                                          
    

    