a=[
    [3,4,5],[33,6,1,2]
]
num=a[0][0]
for i in a:
    for j in i:
        if num>j:
            num=j
print(num)
