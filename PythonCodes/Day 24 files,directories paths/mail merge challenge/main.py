#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

print("Mail merge program")

# with open("./Input/Letters/starting_letter.txt" ,mode="r") as file:
#     print(file.read())

with open("./PythonCodes/Day 24 files,directories paths/mail merge challenge/Input/Letters/starting_letter.txt" ,mode="r") as file:
    print(file.read())


list = []
temporary_file = ""

with open("./PythonCodes/Day 24 files,directories paths/mail merge challenge/Input/Names/invited_names.txt" ,mode="r") as f:
# with open("./Input/Names/invited_names.txt", mode="r") as f:
    # print(f.readlines())
    for name in f:
        # print(name)
        list.append(name)
# print(list)

with open("./PythonCodes/Day 24 files,directories paths/mail merge challenge/Input/Letters/starting_letter.txt" ,mode="r") as f:
# with open("./Input/Letters/starting_letter.txt", mode="r") as f:
    # print(f.read())
    temporary_file = f.read()
# print(temporary_file)

for name in list:
    # print(name)
    new_file = temporary_file.replace("[name]", name)
    file_name = name[:-1]
    # print(file_name)
    with open(f"./PythonCodes/Day 24 files,directories paths/mail merge challenge/Output/ReadyToSend/{file_name}.txt" ,mode="w") as new_letter:
    # with open(f"./Output/ReadyToSend/{file_name}.txt", mode="w") as new_letter:
        new_letter.write(new_file)
