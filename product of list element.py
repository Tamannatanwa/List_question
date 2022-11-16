a=[6,1,3,5,6,3,2]
j=0
pr=1
while j<len(a):
    if a[j]!=6:
        pr=pr*a[j]
    j=j+1
print(pr)
print(pr+30)

