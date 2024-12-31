import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#to get coordinates of each point on the map
# def get_mouse_clk_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_clk_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct",
                                    prompt="Mention the name of the U.S. State not present on the map.").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

#states to learn

screen.exitonclick()