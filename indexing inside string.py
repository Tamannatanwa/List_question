# a=["aniket","tamanna","priya","amrita"]
# i=0
# count=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j],end=" ")
#         count+=1
#         j+=1
#     print()
#     i+=1
# print(count)

a=[[10,20,30],[40,50,60]]
b=len(a)
for i in range(b):
    r=a[i]
    for j in range(len(r)):
        print(i,j,a[i][j])
    print()
        
        