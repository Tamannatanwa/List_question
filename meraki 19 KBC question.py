print("WELCOME TO KBC")
name=input("enter your name:")
question=["1.how many continents are there?"," 2.what is the  capital of india?","3.ng mei koaun se course padhaya jaata hai?"]
option=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.software engineering","2.counseling","3.torium","4.agriculture"]]
solution=[3,4,1]
life_line=[["1.four","2.seven"],["1.bhopal","2.delhi"],["1.softeware engineering","2.counseling"]]
life_solution=[2,2,1]
price=[" YOU ARE WON 1000RUPEES, CONGREATULATION","WOW!,NICE,GREAT ANSWER","AWESOME ,YOU ARE WINNER KBC GAME"]
i=0
index=0
count=0
while i<len(question):
    c=question[i]
    print(c)
    j=0
    while j<len(option[i]):
        n=option[i][j]
        j=j+1
        print(n)
    print("1.with liveline")
    print("2.without liveline")
    choose=int(input("enter you choice="))
    if choose==1:
        if count==0:
            z=0
            while z<len(life_line[i]):
                d=life_line[i]
                z+=1
            print(d)
            count+=1
            choice=int(input("enter your choice="))
            if choice==life_solution[i]:
                    print("you are winner")
                    print(price[i])
            else:
                    print("you are wrong")
                    break
        else:
            print("you are already use lifeline") 
            choice=int(input("enter your choice"))        
            if choice==solution[index]:
                print("you are right")
                print(price[i])
            else:
                print("wrong answer")
                break
    else:
            choice=int(input("enter your choice"))        
            if choice==solution[index]:
                print("you are write")
                print(price[i])
            else:
                print("wrong answer")
                break
    index+=1
    i=i+1