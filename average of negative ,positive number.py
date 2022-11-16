# l=[1,2,3,4,5,6,7,8,9,10]
# i=0
# a=[]
# while i<len(l):
#     s=[l[i],l[i+1]]
#     a.append(s)
#     i=i+2
# print(a)


a=[1,2,3,-2,-4,5,6,-7]
i=0
sum=0
num=0
count=0
co=0
while i<len(a):
    n=a[i]
    if n>0:
        sum+=n
        count+=1
    else:
        num+=n
        co+=1
    i=i+1
average=sum/count
ave=sum/co
print(ave,"negative number average")
print(average,"positive number average")

