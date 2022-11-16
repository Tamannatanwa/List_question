ms=[[8,3,4],
    [1,5,9],
    [6,7,2]]
i=0
sum=0
sum1=0
sum2=0
c1=0
c2=0
c3=0
while i<len(ms):
    sum=sum+ms[i][0]
    sum1=sum1+ms[i][1]
    sum2=sum2+ms[i][2]
    i=i+1
print('total of row 1 =',sum)
print('total of row 2 =',sum1)
print('total of row 3 =',sum2)
if sum==sum1==sum2:
    print("it is magic squear")
else:
    print("it is not magic squear")
    