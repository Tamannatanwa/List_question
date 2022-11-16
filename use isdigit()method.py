# a="ashwini"
# i=0
# b=[]
# while i<len(a):
#     n=a[i]
#     i=i+1
#     b.append(n)
# print(b)

a="tamanna123@navgurukul"
b=''
i=0
c=''
while i<len(a):
    if a[i].isdigit()==True:
        b+=a[i]
    else:
        c+=a[i]
    i=i+1
print(b)
print(c)