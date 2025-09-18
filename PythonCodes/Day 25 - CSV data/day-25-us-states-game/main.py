
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
# print(data)
all_state = data.state.to_list()


guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)} / 50 Guess the State",
                                    prompt="What`s another state`s name?").title()

    if answer_state == "Exit":
        # print(guessed_state)
        missing_state = []

        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        print(missing_state)
        new_date = pandas.DataFrame(missing_state)
        new_date.to_csv("missing_data.csv")
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        # print("got right")
        state_data = data[data.state == answer_state]
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(answer_state)
    else:
        print("not right")



# def my_guess_game():
#     i = 1
#     while i < 51:
#         print(i)
#         answer_state = screen.textinput(title=f"{i} / 50 Guess the State", prompt="What`s another state`s name?")
#         if answer_state == "exit":
#             quit()
#         if answer_state in all_state:
#             print("got right")
#             state_data = data[data.state == answer_state]
#             t = turtle.Turtle()
#             t.hideturtle()
#             t.penup()
#             t.goto(state_data.x.item(), state_data.y.item())
#             t.write(state_data.state.item())
#         else:
#             print("not right")
#
#         i+=1
#
# my_guess_game()
screen.exitonclick()
