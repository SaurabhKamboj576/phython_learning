import random

def game():
    print("you are playing the game..................")
    score = random.randint(1,1000)
    print("Your cureent score is :",score)
    with open("highscore.txt", "r") as file:
        pre_score = file.read()
        if (pre_score == ""):
            previous_score = 0
        else :
            previous_score = int(pre_score)
    file.close()
    if (score > previous_score) or (previous_score == 0):
        with open("highscore.txt", "w")as new:
            new.write(str(score))
        new.close()
        print(f"congratulations you have breaked your previous record , your new score is {score} which is greater then the previous score {previous_score}")
    else :
        print(f"you have performed not well your current score is {score} which is less than previous score {previous_score}")

game()
