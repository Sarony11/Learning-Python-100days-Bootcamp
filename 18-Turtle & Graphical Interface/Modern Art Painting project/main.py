import colorgram
from turtle import Screen, exitonclick, Turtle, left
import random

# Defining objects
tim = Turtle()
screen = Screen()
screen.colormode(255)

# Generating color list from image
rgb_colors = []
colors = colorgram.extract('18-Turtle & Graphical Interface/Modern Art Painting project/image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
    if i <= 3:
        rgb_colors.pop(0)
    i += 1


# Defining variables
dot_size = 20
x_tim=-400
y_tim=-200
x_dots = 10
y_dots = 10
distance = 50

tim.hideturtle()
tim.penup()
tim.goto(x_tim,y_tim)

for i in range(y_dots):
    for i in range(x_dots):
        tim.dot(dot_size,random.choice(rgb_colors))
        tim.forward(distance)
    y_tim += distance
    tim.goto(x_tim,y_tim)

screen = exitonclick()