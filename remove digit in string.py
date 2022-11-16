a="my8 name8 is tamanna"
l=""
i=0
while i<len(a):
    b=a[i]
    if (b>="A" and b<="Z") or (b>=a and b<="z") or b==" ":
        l+=a[i]
    i=i+1
print(l.split())
