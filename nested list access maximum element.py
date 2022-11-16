a=[[4,3,2],[8,1,7,99],[9,87,7,12,56,9000,80000]]
i=0
sum=0
c=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        b=0
        while j<len(a[i]):
            max=0
            if a[i][j]>max:
                max=a[i][j]
                c.append(max)
                k=0
                p=0
                while k<len(c):
                    if c[k]>p:
                        p=c[k]
                    k=k+1    
            j=j+1
    i=i+1
print(p,"is max")