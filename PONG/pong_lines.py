from turtle import Turtle

class Mid_line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.pensize(7)
        self.speed("fastest")

    
    def draw(self):    
        while self.ycor() < 300:
            self.setheading(90)
            self.pencolor("white")
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(20)
