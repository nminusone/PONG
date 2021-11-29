import turtle as t
from turtle import Turtle, Screen
from paddle import Paddle, Ball

screen = Screen()
# Tracer turns animation off
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
pong = Ball()

screen.listen()
screen.onkey(right_paddle.right_up, 'Up')
screen.onkey(right_paddle.right_down, 'Down')
screen.onkey(left_paddle.left_up, 'w')
screen.onkey(left_paddle.left_down, 's')

game_is_on = True
while game_is_on:
    # Updates when animation is off/Tracer(0)
    screen.update()
    pong.move_ball()

screen.exitonclick()
