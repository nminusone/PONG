import turtle as t
from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
right_paddle = Paddle()
screen.listen()
screen.onkey(right_paddle.up, 'Up')

screen.exitonclick()
