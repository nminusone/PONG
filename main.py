import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
# Tracer turns animation off
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
pong = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(right_paddle.right_up, 'Up')
screen.onkey(right_paddle.right_down, 'Down')
screen.onkey(left_paddle.left_up, 'w')
screen.onkey(left_paddle.left_down, 's')

game_is_on = True
moving = True
while game_is_on:
    # Updates when animation is off/Tracer(0)
    time.sleep(pong.ball_speed)
    screen.update()
    pong.move_ball()
    print(pong.speed())
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce()
    elif pong.distance(right_paddle) < 50 and pong.xcor() > 320 or pong.distance(
            left_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_back()
    elif pong.xcor() > 380:
        score.change_left()
        pong.resets()
        time.sleep(1)
        pong.move_ball()
    elif pong.xcor() < -380:
        score.change_right()
        pong.resets()
        time.sleep(1)
        pong.move_ball()
screen.exitonclick()
