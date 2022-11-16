a=int(input("enter the number:"))
b=int(input("enter trhe number:"))
c=int(input("enter the number:"))
if b>a:
    if b>c:
        if c>a:
            print(c,"is middle no.")
        else:
            print(a,"is middle no.")
if a>b:
    if a>c:
        if c>b:
            print(c,"is middle no.")
        else:
            print(b,"is middle")
if c>a:
    if c>b:
        if a>b:
            print(a,"is middle no.")
        else:
            print(b,"is middle number")
            
            

        