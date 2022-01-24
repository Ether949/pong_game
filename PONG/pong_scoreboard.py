from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-100, 200)
        self.l_score = 0
        self.r_score = 0
        self.write(self.l_score, "center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, "center", font=("Courier", 50, "normal"))

    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, "center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, "center", font=("Courier", 50, "normal"))

    
    def score_l(self):
        self.l_score += 1
        self.update_score()


    def score_r(self):
        self.r_score += 1
        self.update_score()
