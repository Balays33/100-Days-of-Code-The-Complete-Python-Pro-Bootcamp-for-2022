from data import resources,MENU



#TODO: 1 Preint resources


def prin_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

#TODO: 2  Prompt user by asking “ What would you like? (espresso/latte/cappuccino):

def coffee_choose():
    user_coffee = input("What would you like? (espresso/latte/cappuccino):")
    if user_coffee == "espresso":
        pass
    elif user_coffee == "latte":
        pass
    elif user_coffee == "cappuccino":
        pass
    else: 
        print("wrong input")

#TODO: Turn off the Coffee Machine by entering “off​ ” to the prompt. 
 
def turn_off_machine():
    pass


#coffee_choose()
prin_resources()
