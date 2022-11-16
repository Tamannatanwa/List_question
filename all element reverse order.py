a=["rajitha","kook","tamanna","mom"]
i=0
while i<len(a):
    n=a[i]
    r=n[::-1]
    if r==a[i]:
        print("polindrom",r)
    else:
        print("not polindrom",r)
    i=i+1