a=[57,54,55,-57,56]
i=0
max=0
min=a[i]
while i<len(a):
    secondmax=max
    n=a[i]
    if n>max:
        max=n
    elif n>secondmax:
        secondmax=n
    elif n<min:
        min=n
    i=i+1
max==secondmax
print(max)
print(secondmax)
print(min)



