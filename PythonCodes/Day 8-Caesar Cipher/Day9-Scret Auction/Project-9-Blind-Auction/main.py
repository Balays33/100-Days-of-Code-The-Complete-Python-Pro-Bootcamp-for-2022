from art import logo
import os

print(logo)
auction ={

}


def infouser():
    name = input("What is your name of the bidden: ")
    bid = input("What is the bid: ")
    auction[name] = bid

def winner():
    winnername = ""
    winnerbid = 0
    for name in auction:
        if winnerbid < int(auction[name]):
            winnerbid = int(auction[name])
            winnername = name
    print(f"The winner is {winnername} and the bid is {winnerbid}")
        

otherbid = True

def runprogi(otherbid):
    """This is the run
    fuction"""
    while otherbid:
        infouser()
        run = input("There are other users who want to bid (yes/no):").lower()
        if run == "no":
            otherbid = False
        os.system('clear')
    winner() 
runprogi(otherbid)
print(auction)