import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
IMAGE = './us-states-game-start/blank_states_img.gif'
FONT = ['Arial', 8, 'normal']
screen.addshape(IMAGE)
turtle.shape(IMAGE)
Andy = turtle.Turtle()
Andy.ht()
Andy.penup()


data = pandas.read_csv('./us-states-game-start/50_states.csv')
states = data.state.to_list()
already_guessed = []
game = True
while game:
    guessed = len(already_guessed)
    answer = screen.textinput(title=f'Guessed {guessed}/50', prompt='What\'s another State\'s name?').title()
    if answer in states and answer not in already_guessed:
        row = data[data.state == answer]
        x_location = int(row.x)
        y_location = int(row.y)
        already_guessed.append(answer)
        Andy.goto(x_location, y_location)
        Andy.write(answer, align='center', font=FONT)
    if already_guessed == len(states):
        game = False

screen.mainloop()