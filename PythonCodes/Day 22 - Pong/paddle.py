from turtle import Turtle

class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=2, stretch_len=1)
        self.penup()
        self.paddle.goto(350,0)

    def go_up():
        pa

