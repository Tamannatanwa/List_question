a=['a','n','i','k','e','t']
count=0
c=0
for i in a:
    if i in "aeiou":
        count+=1
    elif i in "BCDFGHJKLMNPQRSTVWXYZ  bcdfghjklmnpqrstvwxyz":
        c+=1
print("vowel in list:",count)
print("constant in list:",c)






