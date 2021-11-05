from turtle import *
import random


t1 = Turtle(shape='turtle')
t2 = Turtle(shape='turtle')
t3 = Turtle(shape='turtle')
t4 = Turtle(shape='turtle')
t5 = Turtle(shape='turtle')
all_turtles = [t1, t2, t3, t4, t5]

screen = Screen()
colors = ['red', 'blue', 'green', 'yellow', 'orange']

# We use keywords arguments to make the make the code more undestandable
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What turtle do you think is going to win? Enter a color:")

def initial_positions():
    x = -250
    y = -100
    for turtle in all_turtles:
        turtle.penup()
        turtle.goto(x, y)
        turtle.color(colors[all_turtles.index(turtle)])
        turtle.shape('turtle')
        y += 50

def start_the_race():
    end_game = False
    while not end_game:
        for turtle in all_turtles:
            turtle.forward(random.randrange(10))  
            if turtle.xcor() >= 250:
                end_game = True
                print(f'{turtle.fillcolor()} is the winner!')
                return turtle.fillcolor()

def is_the_winner():
    if winner_color == user_bet:
        print('You won!')
    else:
        print('You lost!')

initial_positions()
winner_color = start_the_race()
is_the_winner()

screen.exitonclick()