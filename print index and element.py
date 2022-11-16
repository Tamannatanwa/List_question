a=[[10,20,30],[40,50,60]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(i,j,a[i][j])
        j=j+1
    print()
    i=i+1