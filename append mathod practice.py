a=["tanu","manu"]
b=a.append("pencil")
print(b)



a=[1,2,3,4,5]
a.append("coconut")
print(a)




a=[1,2,3,4,5]
b=a.copy()
a.append(b)
print(a)



a=[1,2,[1,2],3,4,""]
a[2].append("banana")
print(a)

a=[1,2,3,4,5]
a.append(3.0)
a.append(4)
a.append(True)
a.append(False)
print(a)