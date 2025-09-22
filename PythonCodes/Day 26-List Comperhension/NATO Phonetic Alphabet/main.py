student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#Version 1 Balazs version

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato= pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato)
nato_dic = pandas.DataFrame(nato)
# print(nato_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = list(input("What is the message: ").upper())
# print(user_input)
# print([item for item in user_input if item == "a"])


phonetic_code={}
phonetic_cod_list = []

for user_letter in user_input:
    for (index, row) in nato_dic.iterrows():
        if user_letter == row.letter:
            # print(row.code)
            phonetic_code[row.letter] = row.code
            phonetic_cod_list.append(row.code)

print(phonetic_cod_list)

#Version 2 Udemy version

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data= pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = list(input("Enter a word: ").upper())
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)





