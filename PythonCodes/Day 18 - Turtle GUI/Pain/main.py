# import colorgram

# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)

# rgb_color =[]

# for color in colors:
#     r =  color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_color.append(rgb)

# print(rgb_color)

import turtle as t
import random


tim = t.Turtle()
tim.penup()
#tim.goto(-50)
#tim.setposition(-500)
tim.setpos(-100,100)


color_list = [(235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), (196, 77, 19), (217, 133, 177), (193, 164, 15), (34, 106, 166), (11, 21, 62), (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 32, 127), (233, 165, 197), (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232), (229, 73, 45), (169, 180, 229)]
for i in color_list:
    print(i)

a= 2
for y in range(4):
  tim.dot(20,random.choice(color_list))
  for i in range(4):
    #tim.dot(20,random.choice(color2))
    tim.forward(50)
    tim.dot(20,random.choice(color_list))
  if a % 2 == 0:
    tim.right(90)
    tim.forward(50)
    tim.dot(20,random.choice(color_list))
    tim.right(90)
  elif a % 2 !=0 :
    tim.right(-90)
    tim.forward(50)
    tim.dot(20,random.choice(color_list))
    tim.right(-90)
  a+=1


screen = t.Screen()
screen.exitonclick()
