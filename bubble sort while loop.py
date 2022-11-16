a=[12,76,54,34]
i=0
while i<len(a)-1:
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
print(a,"bubble sort")