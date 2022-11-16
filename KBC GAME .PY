print("WELCOME TO KBC GAME")
playername=input("enter your name:")
question=["How many continents are there?","what is the capital of india?","NG mei kaun sa course padhaya jata hai"]
options=[["four","nine","seven","eigth"],["chandigrah","bhopal","chennai","delhi"],["softwere engineering","counselling","tourism","agriculture"]]
i=0
while i<len(question):
    n=question[i]
    print(n)
    j=0
    while j<1:
        c=options[i]
        b=0
        while b<4:
            g=c[b]
            print(g)
            b+=1
        j+=1
    i=i+1
    
    
1