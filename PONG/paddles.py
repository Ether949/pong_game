from turtle import Turtle, ycor

class Paddle(Turtle):

    def __init__(self, x_side):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.goto(x_side, 0)
        self.setheading(90)
    

    def leftup(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(-350, new_y)

    
    def leftdown(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(-350, new_y)
    

    def rightup(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(350, new_y)

    
    def rightdown(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(350, new_y)
