from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()


def place_the_state(state_name):
    state_data = data[data.state == state_name]
    x = int(state_data.x.iloc[0])
    y = int(state_data.y.iloc[0])
    new_state = Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(x, y)
    new_state.write(state_name)


score = 0
num_guesses = 100

game_on = True
while game_on:
    num_guesses -= 1
    guess = screen.textinput(title=f"{score}/50 Guess the state", prompt="Enter a state's name?").title()
    if guess == "Exit":
        break
    if guess in states:
        states.remove(guess)
        score += 1
        place_the_state(guess)

    if score == 50 or num_guesses == 0:
        game_on = False

new_data = pandas.DataFrame(states)
new_data.to_csv("missed_states")
