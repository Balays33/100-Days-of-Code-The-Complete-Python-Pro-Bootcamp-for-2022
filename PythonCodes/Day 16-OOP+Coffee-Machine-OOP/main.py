
#import another_module

#print(another_module.another_variable)

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["City", "Population", "Area"]
table.add_row(["Tokyo", "13,929,286", "2,194 km²"])
table.add_row(["Delhi", "11,007,835", "1,484 km²"])
table.add_row(["Shanghai", "24,870,895", "6,340 km²"])

print(table)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# screen = Screen()
#print(my_screen.canvheight)
# screen.exitonclick()