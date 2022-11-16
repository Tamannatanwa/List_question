kitne_paise_hai=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
count=0
sum=0
num=0
while i<len(kitne_paise_hai):
    n=kitne_paise_hai[i]
    if n>=10000000:
        count+=1
    elif n>=100000:
        sum+=1
    else:
        num+=1
    i=i+1
print(count,"crorpati")
print(sum,"lakhpati")
print(num,"dilwale")