from data import resources,MENU



#TODO: 1 Print resources


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

#TODO: 2  Prompt user by asking “ What would you like? (espresso/latte/cappuccino):

def coffee_choose(user_coffee):
    process = True
    #user_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    
    if user_coffee == "espresso" or user_coffee == "e" or user_coffee == 1:
        #print_out_Menu_order("espresso")
        if check_enough_resources("espresso",process):
            print("We are fine with your order")
            remove_resources("espresso")
        else:
            print("Sorry we are out of resources")
    elif user_coffee == "latte" or user_coffee == "l" or user_coffee == 2:
        if check_enough_resources("latte",process):
            print("We are fine with your order")
            remove_resources("latte")
        else:
            print("Sorry we are out of resources")
    elif user_coffee == "cappuccino" or user_coffee == "c"or user_coffee == 3:
        if check_enough_resources("cappuccino",process):
            print("We are fine with your order")
            remove_resources("cappuccino")
        else:
            print("Sorry we are out of resources")
    else: 
        print("wrong input")

#TODO: 3 Turn off the Coffee Machine by entering “off​ ” to the prompt. 
 
def turn_on_off_machine():
    endOfOperation = False
    while not endOfOperation:

        print("Welcome to the coffee machine! Please take a look at our menu!")
        print("\n1. Espresso: $1.5\n2. Latte: $2.5\n3. Cappuccino: $3.0\n")
        command_selection = input('Select the beverage you would like (1./2./3.) or "report" to display the machine\'s resources ')

        if command_selection == 'report':
            print_resources()
        elif command_selection == 'off':
            endOfOperation = True
        else:
            if command_selection == '1' or command_selection == '2' or command_selection == '3':
                command_selection = int(command_selection)
            else:
                command_selection.lower()

            coffee_choose(command_selection)

def print_out_Menu_order(Menu_item):
    #print(f"You choose {Menu_item}")
    print(MENU[Menu_item])

#TODO: 4 check if the coffe machine has enough resources to make the drink the user selected. 

def check_enough_resources(Menu_item,process):
    
    if resources["water"] >= MENU[Menu_item]["ingredients"]["water"]:
        print("We have enough water")
    else:
        print("Sorry out of water")
        process = False
    if resources["milk"] >= MENU[Menu_item]["ingredients"]["milk"]:
        print("We have enough milk")
    else:
        print("Sorry out of milk")
        process = False
    if resources["coffee"] >= MENU[Menu_item]["ingredients"]["coffee"]:
        print("We have enough coffee")
    else:
        print("Sorry out of coffee")
        process = False
    return process 

#TODO: 5 remove the resources needed to make the drink.
    
def remove_resources(Menu_item):
    resources["water"] -= MENU[Menu_item]["ingredients"]["water"]
    resources["milk"] -= MENU[Menu_item]["ingredients"]["milk"]
    resources["coffee"] -= MENU[Menu_item]["ingredients"]["coffee"]
    #print_resources()
    
    

#coffee_choose()
turn_on_off_machine()

