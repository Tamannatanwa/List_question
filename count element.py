a=["a","s","h","w","i","n","i","m","a","t","p","a","t","i"]
b=[]
i=0
count=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        count+=1
    i=i+1
print(count)




