i=1
while i<6:
    j=1
    while j<=i:
        if j==2:
            print("*",end=" ")
        elif j==4:
            print("*",end=" ")
        else:
            print(i,end=" ")
        j=j+1
    i=i+1
    print()