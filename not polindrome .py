name=["t","a","n","u"]
a=[]
index=-1
same=name
while index>=-len(name):
    num=name[index]
    a.append(num)
    #print(num)
    index-=1
if a==same:
    print(a,"it is polindrome")
else:
    print(a,"it is not  polindrome")