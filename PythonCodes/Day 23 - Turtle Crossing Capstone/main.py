import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Capstone")

turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
loops_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # loops_counter += 1
    # if loops_counter == 1:
    #     car_manager.create_car()
    # elif loops_counter % 6 == 0:
    #     car_manager.create_car()
    car_manager.create_car()
    car_manager.car_move()

    #detect collision with car
    for car in car_manager.all_car:
        if car.distance(turtle) < 20:
            game_is_on = False

    #detect score
    if turtle.is_at_finish_line():
        turtle.reset_position()
        score.add_point()










screen.exitonclick()
