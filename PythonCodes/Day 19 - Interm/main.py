#import turtle as t
import random
from turtle import Turtle, Screen


screen = Screen()
screen.exitonclick()

tim = Turtle()

# def move_right():
#   tim.setheading(0)
#   tim.forward(10)
# def move_left():
#   tim.setheading(180)
#   tim.forward(10)
# def move_up():
#   tim.setheading(90)
#   tim.forward(10)
# def move_down():
#   tim.setheading(270)
#   tim.forward(10)
# def screen_clean_fun():
#   tim.reset()

# screen.onkey(move_right, "Right")
# screen.onkey(move_left, "Left")
# screen.onkey(move_up, "Up")
# screen.onkey(move_down, "Down")

def move_forwards():
  tim.forward(10)
  
def move_backwards():
  tim.backward(10)
  
def move_left():
  new_heading = tim.heading() +10
  tim.setheading(new_heading)
  
def move_right():
  new_heading = tim.heading() +10
  tim.setheading(new_heading)

def screen_clean_fun():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()
  
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

screen.onkey(screen_clean_fun, "c")
screen.listen()






