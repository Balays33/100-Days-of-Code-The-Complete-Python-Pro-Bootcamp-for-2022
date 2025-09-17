import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data)

i = 1
while i < 51:
    # print(i)
    answer_state = screen.textinput(title=f"{i} / 50 Guess the State", prompt="What's another state's name")
    print(answer_state)
    if answer_state == "exit" or answer_state== "Exit":
        quit()

    for dat in data.state:
        # print(dat)
        if answer_state == dat:
            print("good")
            location_x = data[data["state"] == answer_state]
            print(location_x)
            location_y = data[data["state"] == answer_state]
            print(location_y)
    i+=1


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name")
print(answer_state)

for dat in data.state:
    # print(dat)
    if answer_state == dat:
        print("good")





screen.exitonclick()

