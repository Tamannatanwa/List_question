a=["mom","dad","kanha","1221","kook","ram","sita","shyam"]
b=[]
i=0
while i<len(a):
    n=a[i]
    re=n[::-1]
    if re==n:
        print(re,"polindrom")
    else:
        print(re,"not polindrom")
    i=i+1

