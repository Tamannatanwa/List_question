a="my name is rajitha"
b=a.split()
i=0
c=[]
while i<len(b):
    j=0
    while j<len(b[i]):
        if b[i][j]==b[i][0]:
            c.append(b[i][j].upper())
        else:
            c.append(b[i][j])
            
        j=j+1
    i=i+1
d="".join(c)
print([d])