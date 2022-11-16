a=["mom","dad","kanha","1221","kook","ram","sita","shyam"]
b=[]
count=0
for i in a:
    re=i[::-1]
    b.append(re)
    if i==re:
        print(re,"it is polindrom")
        count+=1
    else:
        print(re,"it is not polindrom")
print(count)

