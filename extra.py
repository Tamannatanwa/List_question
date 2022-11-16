l=[11,12,13,14,15,16,17,18,19]
i=0
b=[]
c=-1
while i<(len(l)/2)-2:
    d=[l[i],l[c]]
    b.append(d)
    i=i+1
    c=c-1
print(b)