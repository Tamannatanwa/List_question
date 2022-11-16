a=[50,40,23,70,56,12,5,10,7]
# print(max(a))
index=0
min=a[index]
max=0
while index<len(a):
    num=a[index]
    if num>max:
        max=num
    elif num<min:
        min=num
    index=index+1
print(max)
print(min)