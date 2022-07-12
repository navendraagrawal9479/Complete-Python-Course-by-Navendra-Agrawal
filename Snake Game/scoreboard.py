from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))