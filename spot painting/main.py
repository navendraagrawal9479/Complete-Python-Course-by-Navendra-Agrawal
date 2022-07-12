from turtle import Turtle, Screen, colormode
import random
import colorgram

tom = Turtle()
tom.penup()
colormode(255)
tom.speed("fastest")

colors = colorgram.extract('image.jpg', 20)
turtle_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    turtle_color.append((r, g, b))

tom.setpos(-200, -200)
for _ in range(10):
    for _ in range(10):
        tom.dot(20, random.choice(turtle_color))
        tom.forward(50)

    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(500)
    tom.setheading(0)


screen = Screen()
screen.exitonclick()
