a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
se=0
while i<len(a):
    n=a[i]
    if n%2==0:
        sum+=n
    else:
        se+=n
    i+=1
print(sum,"it is even number")
print(se,"it is odd number")