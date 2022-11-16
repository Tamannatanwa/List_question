a=["archana","devika"]
b=["singh","raj"]
i=0
while i<len(a):
    j=0
    while j<len(b):
        print(a[i][j].upper(),end=" ")
        print(b[i][j].upper(),end=" ")
        j=j+1
        break
    i=i+1