print("Hello the turtles race game")

import random
from turtle import Turtle, Screen


screen = Screen()
screen.exitonclick()

print("Hello turtle race")

tim = Turtle()

movment =[5 , 10 , 15 , 20]
colors  = ["red","green","blue","orange","purple","pink","yellow"]

number_turtles = 4
turtle_racer = {}

for newturtle in range(number_turtles):
  name = "tim"+str(newturtle)
  turtle_racer[name] = Turtle()
 
print(turtle_racer)


def start_position(stpos):
  stpos = stpos
  for name,opj in turtle_racer.items():
    
    print(name)
    print(opj)
    turtle_racer.get(name).penup()
    turtle_racer.get(name).shape("turtle")
    color = random.choice(colors)
    turtle_racer.get(name).color(color)
    turtle_racer.get(name).goto(-100, stpos)
    stpos -= 50
    
  for movin in range(20):
    for name,opj in turtle_racer.items():
      turtle_racer.get(name).forward(random.choice(movment))
      
    
    
      
    
start_position(100)