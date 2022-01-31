import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
image = './us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

pandas.read_cvs('50')


guessed = 0
answer = screen.textinput(title=f'Guessed {guessed}/50', prompt='What\'s another State\'s name?').capitalize()


screen.mainloop()