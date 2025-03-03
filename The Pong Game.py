# The Pong Game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)                                    # Turning off the animation

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        # Needs to bounce
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_points()

    # Detect when left paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_points()

screen.exitonclick()