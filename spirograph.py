import random
from turtle import Turtle, Screen, colormode

tom = Turtle()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color

tom.speed("fastest")
for _ in range(360//5):
    tom.color(random_color())
    tom.circle(100)
    tom.setheading(tom.heading() + 5)

screen = Screen()
screen.exitonclick()