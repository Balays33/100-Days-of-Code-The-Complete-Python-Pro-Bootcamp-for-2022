import turtle as t
import random

tim = t.Turtle()

#tim.forward(100)
#tim.setheading(-90)
#tim.heading()
#tim.forward(100)

def shape_maker(range_number):
  colors  = ["red","green","blue","orange","purple","pink","yellow"] 
  num =4
  
  
  for _ in range(range_number):
    degree = 360 / num
    for _ in range(num):
      tim.forward(100)
      tim.right(degree)
    num +=1
    color = random.choice(colors) #Choose a random color
    tim.color(color)
  
def change_color():
  R = random.randint(0,255)
  G = random.randint(0,255)
  B = random.randint(0,255)
  RGB = (R,G,B)
  return (R,G,B)
  
def random_movment(run_movment):
  direction = [0, 90, 180, 270]
  tim.speed(10)
  tim.pensize(10)
  for _ in range(run_movment):
    tim.color(change_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
  
def make_Sprirograph(pass_degree):
  jump_degree = 360 / pass_degree 
  tim.speed(10)
  for _ in range(int(jump_degree)):
    tim.color(change_color())
    tim.circle(100)
    tim.left(pass_degree)
  
  
  
#shape_maker(8)
#random_movment(100)
make_Sprirograph(30)
  

  
  
