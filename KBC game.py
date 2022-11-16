print("WELCOME TO KON BANEGA CRORPATI GAME ")
username=input("enter your name")
question1=["how many continents are there","what is the capital of india","ng me koun se course padhaye jaate hai"]
option=[["four","nine","seven","eigth"],["chandigrah","bhopal","chennai","delhi"],["software engineering","counseling","tourism","argiculture"]]
life=[["four","seven"],["bhopal","delhi"],["software engineering","counseling"]]
life_solution=[2,2,1]
solution_list=[3,4,1]
i=0
count=0
while i<len(question1):
    print(question1)
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j+=1
    user=("without live line","with live line")
    print("choose your choice")
    print("1.without live line")
    print("2.with live line")
    choice=int(input("your choice="))
    if choice==1:
        user1=int(input("enter your salution="))
        if user1==solution_list[i]:
            print("congrats")
    elif choice==2:
        if count==0:
            k=0
            while k<len(life[i]):
                print(k+1,life[i][k])
                k+=1
            count+=1
            user2=int(input("enter your salution="))
            if user2==life_solution[i]:
                print("congrats")
            else:
                print("wrong answer")
                break
        else:
            print("you have used your lifeline")
            user3=int(input("enter your answer="))
            if user3==solution_list[i]:
                print("congrats")
            else:
                print("wrong answer")
                break
    else:
        print("wrong answer")
        break
    i=i+1