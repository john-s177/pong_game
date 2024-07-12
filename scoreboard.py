from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=("Courier", 30, "normal"))