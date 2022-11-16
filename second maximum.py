a=[50,40,23,70,56,12,5,10,7]
index=0
min=a[index]
max=0
secondmax=0
while index<len(a):
    num=a[index]
    if num>max:
        max=num
    elif num>secondmax:
        secondmax=num
    elif num<min:
        min=num
    index=index+1
# max==secondmax
print(max,"first maximum")
print(secondmax,"second maximum")
print(min,"minimum number")




        
