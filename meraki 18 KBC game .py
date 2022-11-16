print("GAME NAME IS KBC")
name1=input("enter the name=")
print(name1,"WELCOME TO KON BANEGA CARORPATI GAME ")
print("what is the capital of india")
print("A_new delhi")
print("B_kolkata")
print("C_bhopal")
print("D_pune")
option1="A"
option2="B"
option3="C"
option4="D"
q=input("please choose you answer=")
if q==(option1):
    print("your answer is write")
    print("congratulation")
    print("aapne jit liye he 1000 rupees")
else:
    print("you are wrong")
    print("choose any life line")
    print("A.50-50")
    print("B.audience poll")
    print("C.double dip")
    print("D.flip the question")
    option1="A"
    option2="B"
    option3="C"
    option4="D"
    lifeline=input("enter the option=")
    if lifeline==(option1):
        print("you have two option")
        print("A_new delhi")
        print("C_bhopal")
        option1="A"
        option2="C"
        choose=input("enter the option")
        if choose==option1:
            print("your answer is write")
            print("you have now only 3 lifeline left")
            print("aap jit chuke he 1000 rupees")
        elif choose==option2:
            print("wrong answer")
            print("you have now only 3 lifeline left")
    elif lifeline==option2:
        print("you want go to audience side")
        print("A_yes")
        print("B_no")
        option1="A"
        option2="B"
        choose=input("choose your way")
        if choose==option1:
            print("audionce")
        else:
            print("not go to audionce")
    elif lifeline==option3:
        print("you have only 3 lifeline left")
        print("call your realative")
    elif lifeline==option4:
        print("flip this question")
    else:
        print("no one")
