# a=[20,8,12,7,78,92,15]
a=[9,4,10,14,33,556,98]
i=0
b=[]
while i<len(a):
    n=0
    while n<1000:
        j=0
        while j<len(a):
            if a[j]==n:
                b.append(a[j])
            j=j+1
        n=n+1
    i=i+1
    break
print(b)
print("bubble sort")