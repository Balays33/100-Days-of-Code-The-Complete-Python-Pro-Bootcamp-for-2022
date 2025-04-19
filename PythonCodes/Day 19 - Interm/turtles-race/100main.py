from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win add a color")
colors  = ["red","green","blue","orange","purple","pink","yellow"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
  new_turtle = Turtle("turtle")
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x=-230, y=y_position[turtle_index])
  all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
  
#is_race_on = True
  
while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winnig_color == user_bet:
        print("you win")
      else:
        print("you lost")
    rand_direction = random.randint(0,10)
    turtle.forward(rand_direction)
    

screen.exitonclick()
  
  

