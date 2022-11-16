

# a=[4,6,4,3,3,4,3,4,3,8]
# i=0
# b=[]
# k=3
# while i<len(a):
#     if i in a:
#         n=a.count(i)
#         if n>k:
#             if b.count(i)==0:
#                 b.append(i)
#     i=i+1
# print(b)



a=[4,6,4,3,3,4,3,4,3,8]
i=0
b=[]
c=[]
k=3
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        n=a.count(a[i])
        if n>k:
            c.append(a[i])
    i=i+1
print(c)
