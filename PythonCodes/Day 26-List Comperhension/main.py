print("day 26")
# number = [1,2,3]
# new_number = [n+1 for n in number]
# print(new_number)

# name = "Balazs"
# letters_list = [letter for letter in name]
# print(letters_list)

# new_range = [nu*2 for nu in range(1,5)]
# print(new_range)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [ int(string) for string in list_of_strings]
print(numbers)
result = [num for num in numbers if num % 2 == 0]
print(result)