import random 
n = random.randint(1,100)
a = -1
guess = 0
while(a != n):
    guess+=1
    a = int(input("Enter the number :"))
    if (a < n):
        print("please Enter the higher number")
    elif(a >n):
        print("please Enter the lower number")
print(f"you have guessed the right number {n} in {guess} attempts")
