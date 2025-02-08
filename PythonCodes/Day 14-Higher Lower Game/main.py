from art import logo,vs
from game_data import data
import random


#print(logo)
#print(data)
def count_howmany_data():
    count=0
    for i in data:
        count+=1
    print(count)

#count_howmany_data()


MATCH_COUNT =0
#print(data[49]["name"])
print(data[49])

def pick_celebrity(ran_1,ran_2):
    print(f"who has more follower {data[ran_1]['name']} from {data[ran_1]['country']} description: {data[ran_1]['description']}")
    print(vs)
    print(f"who has more follower {data[ran_2]['name']} from {data[ran_2]['country']} description: {data[ran_2]['description']}")
    return data[ran_1], data[ran_2]



def play_game(MATCH_COUNT):
    print(logo)
    cont= True
    while cont:
        ran_1= random.randint(0,49)
        ran_2=random.randint(0,49)
        player_answer_0,player_answer_1 = pick_celebrity(ran_1,ran_2)
        try:
            answer = int(input("Please choose answer A : 1 or answer B : 2 : "))
        except:
            print("Something went wrong")
        if answer == 1:
            print(player_answer_0)
            if player_answer_0['follower_count'] > player_answer_1['follower_count']:
                print("WON")
                cont = True
            else:
                print("LOST")
                print(f'Sorry! That\'s wrong :( \n\nFinal Score: {MATCH_COUNT}')
               
                cont = False
        elif answer == 2:
            print(player_answer_1)
            if player_answer_1['follower_count'] > player_answer_0['follower_count']:
                print("WON")
                cont = True
            else:
                print("LOST")
                print(f'Sorry! That\'s wrong :( \n\nFinal Score: {MATCH_COUNT}')
                cont = False
        MATCH_COUNT+=1
    
play_game(MATCH_COUNT)

    
