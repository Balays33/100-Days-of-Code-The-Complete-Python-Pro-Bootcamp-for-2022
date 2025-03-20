#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password=[]
print(password)
for letter in range(0,nr_letters):
    rand = random.randint(0,26)
    #print(rand)
    for inletter in letters:
        #print(inletter)
        if rand == letters.index(inletter):
            password += inletter
            

print(password)

for insymbols in range(0,nr_symbols):
    rand = random.randint(0,8)
    for insymbols in symbols:
        if rand == symbols.index(insymbols):
            password += insymbols

print(password) 

for innumbers in range(0,nr_numbers):
    rand = random.randint(0,9)
    for innumbers in numbers:
        if rand == numbers.index(innumbers):
            password += innumbers

print(password) 

newpassworld = random.sample(password, len(password))
print(newpassworld)

pas = ""
for newpas in newpassworld:
    pas+= newpas
print(pas)
    






#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P