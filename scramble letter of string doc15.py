
from random import sample


a=["python","list","exrcise","practice","solution"]
#print(a)
b=[''.join(sample(ele,len(ele))) for ele in a]
print("scrambled strings in lists are:"+str(b))


