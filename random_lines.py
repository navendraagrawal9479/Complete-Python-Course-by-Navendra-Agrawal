import random
from turtle import Turtle, Screen, colormode

tom = Turtle()

angles = [0, 90, 180, 270]
colors = ["DeepSkyBlue", "LightGreen", "DarkSlateGray",
          "DarkOrange", "RosyBrown", "DarkOrchid", "DarkSalmon"]

colormode(255)
# turtle_color = (255, 0, 0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color

tom.pensize(10)
tom.speed("fast")

for _ in range(100):
    tom.color(random_color())
    tom.forward(40)
    tom.setheading(random.choice(angles))

screen = Screen()
screen.exitonclick()