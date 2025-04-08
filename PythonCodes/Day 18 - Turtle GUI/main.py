import turtle as t
import random

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



colors  = ["red","green","blue","orange","purple","pink","yellow"] 
num =4

for _ in range(8):
  degree = 360 / num
  for _ in range(num):
    tim.forward(100)
    tim.right(degree)
  num +=1
  color = random.choice(colors) #Choose a random color
  tim.color(color)