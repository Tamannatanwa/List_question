a="python language"
i=0
b=[]
while i<len(a):
    if a[i] in "aioeuAEIOU":
        b.append(a[i])
    i=i+1
print(b)


