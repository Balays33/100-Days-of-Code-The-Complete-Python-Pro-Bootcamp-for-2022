from data import resources,MENU



#TODO: 1 Preint resources


def prin_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

#TODO: 2  Prompt user by asking “ What would you like? (espresso/latte/cappuccino):

def coffee_choose():
    user_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_coffee == "espresso" or user_coffee == "e":
        print_out_Menu_order("espresso")
        if check_enough_resources("espresso"):
            print("We are fine with your order")
            resources["water"] -= MENU[Menu_item]["ingredients"]["water"]
            resources["milk"] -= MENU[Menu_item]["ingredients"]["milk"]
            resources["coffee"] -= MENU[Menu_item]["ingredients"]["coffee"]
            prin_resources()
        else:
            print("Sorry we are out of resources")
    elif user_coffee == "latte" or user_coffee == "l":
        pass
    elif user_coffee == "cappuccino" or user_coffee == "c":
        pass
    else: 
        print("wrong input")

#TODO: Turn off the Coffee Machine by entering “off​ ” to the prompt. 
 
def turn_off_machine():
    pass

def print_out_Menu_order(Menu_item):
    #print(f"You choose {Menu_item}")
    print(MENU[Menu_item])

def check_enough_resources(Menu_item):
    if resources["water"] > MENU[Menu_item]["ingredients"]["water"]:
        print("We have enough water")
    else:
        print("Sorry out of water")
        return False
    if resources["milk"] > MENU[Menu_item]["ingredients"]["milk"]:
        print("We have enough milk")
    else:
        print("Sorry out of milk")
        return False
    if resources["coffee"] > MENU[Menu_item]["ingredients"]["coffee"]:
        print("We have enough coffee")
    else:
        print("Sorry out of coffee")
        return False
    

    

coffee_choose()
#prin_resources()
