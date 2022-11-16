
a="tamann 123 @ navgurukul"
b=''
for i in a:
    if i.isdigit()==True:
        b+=i
print(b)



        

a="tamann 123.0 @navgurukul"
b=''
for i in a:
    if i.isalpha()==True:
        b+=i
print(b)
        
