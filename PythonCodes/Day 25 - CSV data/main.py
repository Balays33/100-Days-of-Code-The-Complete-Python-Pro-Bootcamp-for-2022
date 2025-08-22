"""
data= []

with open("./PythonCodes/Day 25 - CSV data/weather_data.csv", mode= "r") as file:
    # print(file.readlines())
    for line in file:
        # print(line)
        data.append(line)

print(data)
"""
# import csv

# with open("./PythonCodes/Day 25 - CSV data/weather_data.csv", mode= "r") as file:
#     data= csv.reader(file)
#     temperatures = []
#     for row in data:
#         print(row)
#         new_temp = row[1]
#         print(new_temp)
#         if row[1] != "temp":
#             temperatures.append(int(new_temp))
       

# print(temperatures)


import pandas

data = pandas.read_csv("./PythonCodes/Day 25 - CSV data/weather_data.csv")
print(data)