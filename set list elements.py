a = [2,0,4,0,0,1,3,0]
b = a.copy()
for i in b:
    if i == 0:
        a.remove(i)
for i in b:
    if i == 0:
        a = a +[i]
print(a)