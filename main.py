import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
IMAGE = './us-states-game-start/blank_states_img.gif'
screen.addshape(IMAGE)
turtle.shape(IMAGE)

FONT = ['Arial', 8, 'normal']

Andy = turtle.Turtle()
Andy.ht()
Andy.penup()

data = pandas.read_csv('./us-states-game-start/50_states.csv')
states = data.state.to_list()
already_guessed = []
game = True
while len(already_guessed) < len(states):
    guessed = len(already_guessed)
    answer = screen.textinput(title=f'Guessed {guessed}/50', prompt='What\'s another State\'s name?').title()
    if answer in states and answer not in already_guessed:
        row = data[data.state == answer]
        x_location = int(row.x)
        y_location = int(row.y)
        already_guessed.append(answer)
        Andy.goto(x_location, y_location)
        Andy.write(answer, align='center', font=FONT)
    elif answer == 'Exit':
        break

missed = [state for state in states if state not in already_guessed]
new_data = pandas.DataFrame(missed)
new_data.to_csv('States to learn')

screen.mainloop()
