file = open("PythonCodes/Day 24 files,directories paths/file system/my_file.txt")
#file = open("./my_file.txt")
content = file.read()
print(content)
file.close()


#Same 

with open("PythonCodes/Day 24 files,directories paths/file system/my_file.txt") as file:
    content = file.read()
    print(content)

with open("PythonCodes/Day 24 files,directories paths/file system/my_file.txt", mode ="w") as file:
    file.write("New text")

with open("PythonCodes/Day 24 files,directories paths/file system/my_file.txt", mode ="a") as file:
    file.write("this is add new file")

# no file i have create a new txt file
with open("PythonCodes/Day 24 files,directories paths/file system/new_my_file.txt", mode ="w") as file:
    file.write("I have created a new file")


