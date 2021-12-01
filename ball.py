from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.ball_speed = 0.09
        self.resets()
        self.x_plus = 10
        self.y_plus = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_plus
        new_y = self.ycor() + self.y_plus
        self.speed(self.ball_speed)
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_plus *= -1

    def resets(self):
        self.goto(0, 0)
        self.ball_speed = 0.09

    def bounce_back(self):
        self.x_plus *= -1
        self.ball_speed /= 1.3
