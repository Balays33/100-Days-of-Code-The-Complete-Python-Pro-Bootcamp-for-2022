import random
import hangman_art,hangman_words

print(hangman_art.logo)

#print(hangman_art.stages[1])

world = random.choice( hangman_words.word_list)
print(world)
das = len(world)
#print(das)
guees_world = []
for c in world:
    guees_world.append(c)
print(guees_world)
myworld =[]
for printdas in range(0,das):
    myworld.append("_")
print(myworld)




life = 6

while life > 0:
    print(f"your life is : {life}")
    guess_caracter = input("What is your caracter:")
    keeplife = False
    for check in guees_world:
        #print(check)
        if guess_caracter == check:
            myworld[guees_world.index(check)] = guess_caracter
            keeplife = True
        print(myworld)

    if myworld == guees_world:
        print("you win")
        break
    if keeplife == False:
        life -=1
    print(hangman_art.stages[life])
if life == 0:
    print("you lost")

