from turtle import Turtle, Screen, exitonclick
import random

tim = Turtle()
screen = Screen()

tim.shape("arrow")

""" tim.color('red', 'yellow')
tim.begin_fill()
while True:
    tim.forward(200*2)
    tim.left(170)
    if abs(tim.pos()) < 1:
        break
tim.end_fill()
screen.mainloop() """

""" for i in range(4):
    tim.forward(100)
    tim.left(90) """

""" for i in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10) """

""" for i in range(3,20):
    lenght = 50
    angle = 360 / i
    screen.colormode(255)
    r = random.randrange(1,255)
    g = random.randrange(1,255)
    b = random.randrange(1,255)
    color = (r,g,b)
    print(color)
    tim.pencolor(color)
    for a in range(i):
        tim.forward(lenght)
        tim.right(angle)
 """

""" def new_direction():
    direction = random.randrange(4)
    if direction == 0:
        return None
    elif direction == 1:
        tim.right(90)
    elif direction == 2:
        tim.right(180)
    elif direction == 3:
        tim.left(90)

    def random_colour():
        r = random.randrange(1,255)
        g = random.randrange(1,255)
        b = random.randrange(1,255)
        color = (r,g,b)
        return color

tim.speed(25)
tim.width(5)
screen.colormode(255)

while True:
    r = random.randrange(1,255)
    g = random.randrange(1,255)
    b = random.randrange(1,255)
    color = (r,g,b)
    tim.pencolor(color)
    new_direction()
    tim.forward(15) """

def random_colour():
    r = random.randrange(1,255)
    g = random.randrange(1,255)
    b = random.randrange(1,255)
    color = (r,g,b)
    return color

r = 100
screen.colormode(255)
number_circles = 100
tim.speed(25)
for i in range(number_circles):
    tim.pencolor(random_colour())
    tim.circle(r)
    tim.right(360/number_circles)


screen = exitonclick()