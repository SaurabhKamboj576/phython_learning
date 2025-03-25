'''
1  then snake
0 then water
-1 then gun
'''
import  random
computer = random.choice([1,-1,0])
firstDictionery = {"S": 1 , "W": 0, "G":-1,"s": 1 , "w": 0, "g":-1}
yourchoice = input("Enter only one letter from S (Snake), W(water) and G(Gun) :")
yourvalue = firstDictionery[yourchoice]
ReverseDictionery = {1 :"Snake", 0: "Water",-1:"Gun"}
computerchoice = ReverseDictionery[computer]
print("Computer Choise :", computerchoice)

if (computer == yourvalue):
    print("it's a draw")
else :
    if (computer == 1) and (yourvalue == -1):
        print("you win")
    elif (computer == 1) and (yourvalue == 0):
        print("you loss")
    elif (computer == 0) and (yourvalue == -1):
        print("you win")
    elif (computer == 0) and (yourvalue == 1):
        print("you win")
    elif (computer == -1) and (yourvalue == 0):
        print("you loss")
    else :
        print("you loss")







