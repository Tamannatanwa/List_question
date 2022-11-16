


a="the quick brown fox jumped over the lazy dog.the dog slept over the verandah"
i=0
b=""
c=a.split()
while i<len(c):
    if c[i]!="over":
        b=b+c[i]
        b=b+" "
    i=i+1
print(b)


