from turtle import Turtle, Screen

tom = Turtle()


def go_forward():
    tom.forward(20)


def go_backward():
    tom.backward(20)


screen = Screen()
screen.listen()
screen.onkey(go_forward, "Right")
screen.onkey(go_backward, "Left")
screen.exitonclick()
