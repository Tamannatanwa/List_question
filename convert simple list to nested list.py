a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
i=0
b=[]
while i<3:
    j=i
    c=[]
    while j<len(a):
        n=a[j]
        c.append(n)
        j+=3
    b.append(c)
    i=i+1
print(b)
        
    
    
