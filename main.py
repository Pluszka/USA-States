import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
image = './us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('./us-states-game-start/50_states.csv')
states = data.state.to_list()
already_guessed = []
guessed = len(already_guessed)
game = True
while game:
    answer = screen.textinput(title=f'Guessed {guessed}/50', prompt='What\'s another State\'s name?').capitalize()
    if answer in states and answer not in already_guessed:

        already_guessed.append(answer)
    if already_guessed = len(states):
        game = False

screen.mainloop()