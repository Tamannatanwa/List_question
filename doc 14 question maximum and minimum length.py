


# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# index=0
# max=a[index]
# while i<len(a):
#     num=a[i]
#     if num>max:
#         max=num
#     i=i+1
# print(max)
    
            

a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
maximum=a[i]
while i<len(a):
    num=len(a[i])
    max=len(a[i])
    if num>max:
        max=num
    if a[i]>maximum:
        maximum=a[i]
    i=i+1
a=max,maximum
v=tuple(a)
# print(max,maximum)
print(v)


    
            


