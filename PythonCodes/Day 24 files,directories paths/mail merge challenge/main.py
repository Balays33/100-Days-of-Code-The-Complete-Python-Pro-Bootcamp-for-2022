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
