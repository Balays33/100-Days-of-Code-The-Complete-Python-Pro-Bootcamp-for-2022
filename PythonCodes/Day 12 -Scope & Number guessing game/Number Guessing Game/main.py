from art import logo
import random

#print(logo)

number = random.randint(1,100)
#print(number)

level = [10, 5]

chooselevel = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
gamelevel = 0
if chooselevel == "easy":
    gamelevel = level[0]
elif chooselevel == "hard":
    gamelevel = level[1]
else:
    print("wrong input")
    print("your game lavel is easy")
    gamelevel = level[0]
#print(gamelevel)



def checknumbers(number,gamelevel):
    while gamelevel > 0:
        userguessNumber = int(input("what is your guessing number: "))
        print(userguessNumber)
        if userguessNumber == number:
            print("You found the number")
            print("You WON")
            gamelevel = 1
        elif userguessNumber > number:
            print("Your number is too big")
        elif userguessNumber < number:
            print("Your number is too small")
        gamelevel -= 1
        print(f"You have {gamelevel} live left ")
        
checknumbers(number,gamelevel)
print(f"This was the number {number}")

    

