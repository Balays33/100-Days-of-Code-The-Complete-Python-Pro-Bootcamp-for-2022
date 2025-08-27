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


# import pandas

# data = pandas.read_csv("./PythonCodes/Day 25 - CSV data/weather_data.csv")
# print(data)

import pandas
print("Day 25")

data =pandas.read_csv("/home/user/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2022/PythonCodes/Day 25 - CSV data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
# print(black)

data_dict = {
    "Fur Color" : ["Gray" , "Cinnamon", "Black" ],
    "Count" : [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")