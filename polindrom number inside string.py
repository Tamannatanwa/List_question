a=["mom","madam","papa","sir","naman","nitin"]
count=0
i=0
while i<len(a):
    num=a[i]
    re=num[::-1]
    if a[i]==re:
        print(re,"it is polindrom")
        count+=1
    else:
        print(re,"it is not polindrom")
    i=i+1
print(count,"count palindrom number")


