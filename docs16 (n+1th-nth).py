#t=[1,2,3,4,5,6,7,8,9,10]
# t=[2,4,6,8]
# # c=[]
# for i in range(len(t)-1):
#     v = t[i+1]-t[i]
#     c.append(v) 
# print(c)





a=[2,4,6,8]
c=[]
i=0
while i<len(a)-1:
    num=a[i]
    n=a[i+1]-a[i]
    c.append(n)
    i=i+1
print(c)
    
