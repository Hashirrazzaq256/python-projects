import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states = []
missed_states= []


while len(states) < 50:
    answer_state = screen.textinput(title=f"{len(states)}/50 correct ", prompt="What is another state's name")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        for g in all_states:
            if g not in states:
                missed_states.append(g)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("Missed_states.csv")
        break

    if answer_state in all_states:
        states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == answer_state]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(answer_state)







# turtle.mainloop()

