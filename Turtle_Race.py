from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500,height = 400)
turtle_colors = ["red", "blue", "green", "purple", "yellow", "brown"]
y_coordinate = [-150, -100, -50, 50, 100, 150]
turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.setpos(-230, y_coordinate[turtle_index])
    new_turtle.speed("fastest")
    turtles.append(new_turtle)

user_choice = screen.textinput("Turtle Race.", "Choose your turtle:")

is_game_on = True
while is_game_on:
    for t in turtles:
        if t.xcor()>230:
            is_game_on = False
            if t.pencolor() == user_choice:
                print("You are the winner.")
            else:
                print(f"You lose. The turtle with color {t.pencolor()} has won the race.")
        t.forward(random.randint(0, 15))


screen.exitonclick()
