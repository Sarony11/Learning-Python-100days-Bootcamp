from custom_turtle import classTurtle
from turtle import Turtle, Screen

timmy = classTurtle

print(timmy.legs)
timmy.shell = False
print(timmy.shell)
print(timmy.type)

timmy.run()

jonny = Turtle()
print(jonny)
jonny.shape("turtle")
jonny.color("coral")
jonny.forward(100)
jonny.right(90)
jonny.forward(100)
jonny.forward(100)
jonny.left(90)
jonny.forward(100)
jonny.right(90)
jonny.forward(100)
jonny.right(90)
jonny.forward(300)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
