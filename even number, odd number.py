elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
count=0
co=0
while i<len(elements):
    n=elements[i]
    if n%2==0:
        count+=1
    else:
        co+=1
    i=i+1
print(co,"odd numbers")
print(count,"even numbers")