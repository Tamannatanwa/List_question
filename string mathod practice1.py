a="tamanna123@tanwar"
b=''
i=0
while i<len(a):
    if a[i].isalpha()==True:
        b+=a[i]
    i=i+1
print(b)



a="tamanna123@tanwar"
b=''
i=0
while i<len(a):
    if a[i].isalnum()==True:
        b+=a[i]
    i=i+1
print(b)


a="tamanna123@tanwar"
b=''
i=0
while i<len(a):
    if a[i].islower()==True:
        b+=a[i]
    i=i+1
print(b)



a="Tamanna123@Tanwar"
b=''
i=0
while i<len(a):
    if a[i].isupper()==True:
        b+=a[i]
    i=i+1
print(b)



a="Tamanna123@Tanwar"
b=''
i=0
while i<len(a):
    if a[i].istitle()==True:
        b+=a[i]
    i=i+1
print(b)



a="tamanna was good girl"
b=a.replace("was","is")
print(b)



a="tamanna" "is" "good" "girl"
b="".join(a)
print(b)



a="s o s o"
b=a.split()
print(b)
