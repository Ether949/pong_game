from turtle import Turtle, Screen
from pong_lines import Mid_line
from paddles import Paddle
from pong_ball import Ball
import time
from pong_scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("E's Pong")
lines = Mid_line()
lines.draw()

paddle1 = Paddle(-350)
paddle2 = Paddle(350)
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddle1.leftup, "w")
screen.onkey(paddle1.leftdown, "s")
screen.onkey(paddle2.rightup, "Up")
screen.onkey(paddle2.rightdown, "Down")

speed = 1
on = True
while on:
    time.sleep(0.015)
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
       ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() < -320 or ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        speed += 1
        ball.speed(speed)
    
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.score_l()
    
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.score_r()


screen.exitonclick()
