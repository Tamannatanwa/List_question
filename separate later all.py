# a="tamanna"
# b=[]
# i=0
# while i<len(a):
#     n=a[i]
#     b.append(n)
#     i=i+1
# print(b)



# a="tamanna"
# b=""
# i=0
# while i<len(a):
#     n=a[i]
#     b+="'"
#     b+=n
#     b+="'"
#     b+=","
#     i=i+1
# print(b)


a="tamanna"
i=0
b=""
while i<len(a):
        b=b+"'"+a[i]+"'"+","
        i=i+1
        
print(b[:-1])
