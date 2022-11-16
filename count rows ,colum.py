l=[[1, 2],[2, 4]]
i=0
co=0
while i<len(l):
    co+=1
    j=0
    count=0
    while j<len(l[i]):
        count+=1
        j=j+1
    i=i+1
print(co,"rows")
print(count,"colums")