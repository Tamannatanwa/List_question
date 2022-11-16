a=[1,2,3,4,5]
b=a.extend("pen")
print(b)



v=[1,2,3,4]
c=[4,3,2,1]
c.extend(c)
v.extend(c)
print(c)
print(v)



a=[1,2,3,4]
b=[0,0,0,0]
a.extend(b)
print(a)

a=["banana","mango"]
a.extend("areeating")
print(a)



a=[1,2,3,4,5]
b=["banana","apple"]
a.extend(b+a)
print(a)